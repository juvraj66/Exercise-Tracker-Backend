from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from .permissions import IsAdminReadWrite, IsCreatorOrReadOnly1, IsAdminWriteUserRead
from myapp.serializers import ExerciseSerializer, UserExerciseSerializer, LoginSerializer, RegisterSerializer, \
    UserProfileSerializer
from .models import Exercise, UserExercise
from rest_auth.views import LoginView
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from django_filters.rest_framework import FilterSet
from rest_auth.registration.views import RegisterView
from rest_auth.registration.views import VerifyEmailView
from django.contrib.auth.models import User


class LoginView(LoginView):
    serializer_class = LoginSerializer


class Register(RegisterView):
    serializer_class = RegisterSerializer


class UserProfileView(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.all().filter(id=self.request.user.id)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.all().filter(id=self.request.user.id)


# All exercises available
class ExerciseList(generics.ListCreateAPIView):
    filter_fields = ('muscle_group',)
    ordering_fields = ('exercise_name',)
    search_fields = ('exercise_name',)
    permission_classes = (IsAdminWriteUserRead,)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


# Individual exercises
class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminReadWrite,)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseUserList(generics.ListCreateAPIView):
    serializer_class = UserExerciseSerializer
    search_fields = ('u_exercise__exercise_name',)
    ordering_fields = ('updated_at',)

    def get_queryset(self):
        return UserExercise.objects.all().filter(user=self.request.user)


class ExerciseUserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly1,)
    serializer_class = UserExerciseSerializer

    def get_queryset(self):
        return UserExercise.objects.all().filter(user=self.request.user)

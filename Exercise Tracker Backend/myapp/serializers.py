from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Exercise, UserExercise
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class RegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])


class LoginSerializer(LoginSerializer):
    email = None


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creator', 'exercise_name', 'muscle_group', 'muscle', 'equipment')
        model = Exercise


class UserExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.ReadOnlyField(source='u_exercise.exercise_name')
    muscle_group = serializers.ReadOnlyField(source='u_exercise.muscle_group')

    class Meta:
        fields = '__all__'
        model = UserExercise

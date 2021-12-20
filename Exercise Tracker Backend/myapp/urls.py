from django.urls import path
from rest_auth.registration.views import VerifyEmailView
from .views import ExerciseList, ExerciseDetail, ExerciseUserList, ExerciseUserDetail, LoginView, RegisterView, \
    UserProfileView, UserProfileDetailView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', RegisterView.as_view()),
    path('user/', UserProfileView.as_view()),
    path('user/<int:pk>/', UserProfileDetailView.as_view()),
    path('exercises/<int:pk>/', ExerciseDetail.as_view()),
    path('exercises/', ExerciseList.as_view()),
    path('notebook/', ExerciseUserList.as_view()),
    path('notebook/<int:pk>/', ExerciseUserDetail.as_view()),
]

from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Exercise(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200, unique=True)
    muscle_group = models.CharField(max_length=200)
    muscle = models.CharField(max_length=200)
    equipment = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise_name


class UserExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    u_exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    weight = models.CharField(max_length=6)
    reps = models.CharField(max_length=6)
    unit = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.u_exercise} {self.created_at}'

from django.contrib import admin
from .models import Exercise, SubmittedExercise

admin.site.register(Exercise)
admin.site.register(SubmittedExercise)
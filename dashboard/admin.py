from django.contrib import admin
from .models import EnrolledStudent, Major, Teacher

admin.site.register(EnrolledStudent)
admin.site.register(Major)
admin.site.register(Teacher)
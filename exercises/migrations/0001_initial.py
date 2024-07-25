# Generated by Django 5.0.7 on 2024-07-23 08:00

import django.db.models.deletion
import django_ckeditor_5.fields
import exercises.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0008_alter_teacher_teacher_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('slug', models.SlugField(max_length=255)),
                ('uploaded_files', models.FileField(upload_to=exercises.models.uploadPath)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('for_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.major')),
                ('for_students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-26 14:57

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
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
                ('uploaded_files', models.FileField(upload_to='exercises/')),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('for_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.major')),
                ('for_students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.FileField(blank=True, null=True, upload_to='submitted/')),
                ('typed_answer', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=10)),
                ('submitted_at', models.DateTimeField(null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

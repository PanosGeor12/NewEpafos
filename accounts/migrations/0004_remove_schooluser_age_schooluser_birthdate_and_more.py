# Generated by Django 5.0.7 on 2024-07-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_schooluser_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooluser',
            name='age',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Manager', 'Manager')], max_length=20),
        ),
    ]

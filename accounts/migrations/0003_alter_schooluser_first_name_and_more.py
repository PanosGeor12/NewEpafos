# Generated by Django 5.0.7 on 2024-07-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_schooluser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]

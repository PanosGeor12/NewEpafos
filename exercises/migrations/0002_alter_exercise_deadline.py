# Generated by Django 5.0.7 on 2024-07-31 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='deadline',
            field=models.DurationField(),
        ),
    ]

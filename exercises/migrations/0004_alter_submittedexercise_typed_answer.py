# Generated by Django 5.0.7 on 2024-07-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_submittedexercise_typed_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedexercise',
            name='typed_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]

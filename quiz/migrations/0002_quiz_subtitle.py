# Generated by Django 3.1.7 on 2021-03-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='subtitle',
            field=models.CharField(blank=True, max_length=144),
        ),
    ]

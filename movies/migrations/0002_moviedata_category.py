# Generated by Django 5.0 on 2023-12-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='category',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
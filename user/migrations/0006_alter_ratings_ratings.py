# Generated by Django 3.2 on 2025-05-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_ratings_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='ratings',
            field=models.IntegerField(),
        ),
    ]

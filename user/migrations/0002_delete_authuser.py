# Generated by Django 5.0.1 on 2024-02-02 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-05 22:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='universitycampus',
            options={'verbose_name_plural': 'University Campus'},
        ),
        migrations.AlterModelManagers(
            name='universitycampus',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]

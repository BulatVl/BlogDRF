# Generated by Django 4.1.7 on 2023-03-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

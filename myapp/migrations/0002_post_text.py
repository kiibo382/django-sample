# Generated by Django 3.0.7 on 2020-06-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='SOME CATEGORY'),
        ),
    ]
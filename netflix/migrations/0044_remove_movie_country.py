# Generated by Django 4.0.3 on 2022-07-20 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0043_delete_uservisit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
    ]
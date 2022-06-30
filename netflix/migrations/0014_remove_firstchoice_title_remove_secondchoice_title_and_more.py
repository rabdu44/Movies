# Generated by Django 4.0.3 on 2022-06-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0013_firstchoice_title_secondchoice_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstchoice',
            name='title',
        ),
        migrations.RemoveField(
            model_name='secondchoice',
            name='title',
        ),
        migrations.AddField(
            model_name='poll',
            name='firstchoice_title',
            field=models.CharField(default='Yes', max_length=255, verbose_name='Frst Choice Title'),
        ),
        migrations.AddField(
            model_name='poll',
            name='secondchoice_title',
            field=models.CharField(default='No', max_length=255, verbose_name='Second Choice Title'),
        ),
    ]
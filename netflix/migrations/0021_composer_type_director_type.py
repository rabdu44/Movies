# Generated by Django 4.0.3 on 2022-06-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0020_actor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='type',
            field=models.CharField(default='Composer', max_length=255, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='director',
            name='type',
            field=models.CharField(default='Director', max_length=255, verbose_name='Type'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-06-24 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0021_composer_type_director_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='composer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.composer'),
        ),
        migrations.AddField(
            model_name='poll',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.director'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.actor'),
        ),
    ]
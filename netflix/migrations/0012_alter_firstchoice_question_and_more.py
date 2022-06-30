# Generated by Django 4.0.3 on 2022-06-22 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0011_poll_alter_firstchoice_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstchoice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.poll'),
        ),
        migrations.AlterField(
            model_name='secondchoice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.poll'),
        ),
    ]
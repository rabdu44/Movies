# Generated by Django 4.0.3 on 2022-06-11 19:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cast/', verbose_name='Image')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Cast',
            },
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(
                    upload_to='composers/', verbose_name='Image')),
                ('name', models.CharField(max_length=255, verbose_name='Composer Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Music Composer',
                'verbose_name_plural': 'Music Composers',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(
                    upload_to='directors/', verbose_name='Image')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='genres/', verbose_name='Image')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='IMDb_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(
                    0.0), django.core.validators.MaxValueValidator(10.0)])),
            ],
            options={
                'verbose_name': 'IMDb Rating',
                'verbose_name_plural': 'IMDb Ratings',
            },
        ),
        migrations.CreateModel(
            name='Other_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=3.5, validators=[django.core.validators.MinValueValidator(
                    0.0), django.core.validators.MaxValueValidator(10.0)])),
            ],
            options={
                'verbose_name': 'Other Rating',
                'verbose_name_plural': 'Other Ratings',
            },
        ),
        migrations.CreateModel(
            name='Rotten_Tomatoes_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=0, max_digits=3, validators=[
                 django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'Rotten Tomatoes Rating',
                'verbose_name_plural': 'Rotten Tomatoes Ratings',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True,
                 upload_to='user/pictures/', verbose_name='Profile Picture')),
                ('email', models.EmailField(blank=True,
                 max_length=254, unique=True, verbose_name='Email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True,
                 upload_to='posters/', verbose_name='Poster')),
                ('movie', models.FileField(
                    upload_to='movies/', verbose_name='Movie Copy')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('budget', models.CharField(default='20 million',
                 max_length=255, verbose_name='Budget')),
                ('box_office', models.CharField(default='1.50 billion',
                 max_length=255, verbose_name='Box Office')),
                ('date', models.DateField(
                    default=django.utils.timezone.now, verbose_name='Release Date')),
                ('Quality', models.CharField(default='720p',
                 max_length=255, verbose_name='Quality')),
                ('runtime', models.CharField(default='1h 20m',
                 max_length=255, verbose_name='Runtime')),
                ('publication', models.BooleanField(
                    default=True, verbose_name='Publication')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
                ('cast', models.ManyToManyField(blank=True,
                 to='netflix.actor', verbose_name='Cast')),
                ('composers', models.ManyToManyField(blank=True,
                 to='netflix.composer', verbose_name='Composers')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 to='netflix.director', verbose_name='Director')),
                ('genre', models.ManyToManyField(blank=True,
                 to='netflix.genre', verbose_name='Genre')),
                ('imdb_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 to='netflix.imdb_rating', verbose_name='IMDb Rating')),
                ('other_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 to='netflix.other_rating', verbose_name='Other Rating')),
                ('rotten_tomatoes_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 to='netflix.rotten_tomatoes_rating', verbose_name='Rotten Tomatoes Rating')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='Date')),
                ('publication', models.BooleanField(
                    default=True, verbose_name='Publication')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='netflix.movie', verbose_name='Movie')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]

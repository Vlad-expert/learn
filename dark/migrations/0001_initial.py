# Generated by Django 4.0.3 on 2022-03-09 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('active', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create', models.DateField()),
                ('slug', models.SlugField(max_length=255)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dark.band')),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('text', models.TextField()),
                ('MusicAlbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dark.musicalbum')),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dark.band')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dark.band')),
            ],
        ),
    ]
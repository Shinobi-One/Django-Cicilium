# Generated by Django 4.1.2 on 2023-02-23 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='Images')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

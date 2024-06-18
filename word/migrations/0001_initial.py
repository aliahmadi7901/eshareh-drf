# Generated by Django 5.0.6 on 2024-06-18 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان کلمه')),
                ('pronunciation_of_the_word', models.CharField(max_length=100, verbose_name='تلفظ کلمه')),
                ('image', models.ImageField(upload_to='words', verbose_name='تصویر کلمه')),
                ('video_url', models.URLField(verbose_name='url ویدیو')),
            ],
            options={
                'verbose_name': 'کلمه',
                'verbose_name_plural': 'کلمات',
            },
        ),
        migrations.CreateModel(
            name='CategorizeWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان دسته بندی')),
                ('icon', models.FileField(upload_to='categorize', verbose_name='آیکون')),
                ('url_title', models.URLField(verbose_name='عنوان در url')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorize_words', to='word.categorizeword', verbose_name='والد')),
            ],
            options={
                'verbose_name': 'دسته بندی کلمه',
                'verbose_name_plural': 'دسته بندی کلمات',
            },
        ),
    ]

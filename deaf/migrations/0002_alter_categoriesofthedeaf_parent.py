# Generated by Django 5.0.6 on 2024-08-21 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deaf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriesofthedeaf',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_deaf', to='deaf.categoriesofthedeaf', verbose_name='والد'),
        ),
    ]

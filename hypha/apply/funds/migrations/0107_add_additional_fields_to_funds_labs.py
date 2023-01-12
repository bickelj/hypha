# Generated by Django 3.2.16 on 2023-01-09 10:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_customimage_file_hash'),
        ('funds', '0106_applicationsubmission_is_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationbase',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicationbase',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='applicationbase',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='labbase',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='labbase',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='labbase',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

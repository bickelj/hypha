# Generated by Django 2.0.9 on 2019-02-07 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_allow_blank_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpagerelatedpage',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
    ]

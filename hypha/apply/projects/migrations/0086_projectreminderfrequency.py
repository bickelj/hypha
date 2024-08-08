# Generated by Django 4.2.11 on 2024-08-08 20:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("application_projects", "0085_alter_projectsettings_paf_approval_sequential"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectReminderFrequency",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("reminder_days", models.IntegerField()),
                (
                    "relation",
                    models.CharField(
                        choices=[("BE", "Before"), ("AF", "After")],
                        default="BE",
                        max_length=2,
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reminder_frequencies",
                        to="application_projects.projectsettings",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]

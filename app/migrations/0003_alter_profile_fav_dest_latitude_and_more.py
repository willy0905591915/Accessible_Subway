# Generated by Django 4.2.16 on 2024-10-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="fav_dest_latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fav_dest_longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fav_source_latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fav_source_longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="fav_station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.station",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="home_latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="home_longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="work_latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="work_longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

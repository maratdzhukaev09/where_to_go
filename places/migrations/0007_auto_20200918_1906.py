# Generated by Django 3.0.8 on 2020-09-18 16:06

from django.db import migrations


def change_none_to_empty_str(apps, schema_editor):
    Place = apps.get_model('places', 'Place')
    for place in Place.objects.all():
        if place.short_description is None:
            place.short_description = ''
        if place.long_description is None:
            place.long_description = ''
        place.save()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200809_2248'),
    ]

    operations = [
        migrations.RunPython(change_none_to_empty_str)
    ]

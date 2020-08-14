from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests, os
from where_to_go.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Load places from json files to database'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='+', type=str)

    def handle(self, *args, **options):
        json_url = options['json_url'][0]
        response = requests.get(json_url)
        place_info = response.json()
        place = Place.objects.get_or_create(title=place_info['title'], defaults={
            'short_description': place_info['description_short'],
            'long_description': place_info['description_long'],
            'lat': place_info['coordinates']['lat'],
            'lon': place_info['coordinates']['lng'],
        })[0]
        if os.path.exists(os.path.join(BASE_DIR, 'media')):
            for image in place.images.all():
                os.remove(os.path.join(BASE_DIR, image.image.path))
        place.images.all().delete()
        for image_number, image_url in enumerate(place_info['imgs']):
            filename = image_url.split('/')[-1]
            response = requests.get(image_url)
            content = ContentFile(response.content)
            image_object = Image()
            image_object.image.save(filename, content, save=True)
            image_object.place = place
            image_object.number = image_number + 1
            image_object.save()

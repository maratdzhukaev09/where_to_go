from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Place, Image
import json


def show_map(request):
    features = []
    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place-json", args=[place.id])
            }
        }
        features.append(feature)
    places_info = {
      "type": "FeatureCollection",
      "features": features
    }

    context = {
        "places_info": places_info,
    }
    return render(request, "index.html", context)


def show_post_json(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }

    return HttpResponse(json.dumps(place_details, ensure_ascii=False),
                        content_type="application/json")

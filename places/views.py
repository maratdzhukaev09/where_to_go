from django.shortcuts import render
from .models import Place, Image


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
                "detailsUrl": "static/places/moscow_legends.json"
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
    return render(request, 'index.html', context)

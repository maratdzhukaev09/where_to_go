from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)

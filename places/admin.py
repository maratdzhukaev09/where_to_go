from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

    fields = ['image', 'get_preview', 'number', 'place']
    readonly_fields = ['get_preview']

    def get_preview(self, image):
        return format_html('<img src="{}" height=200px />', image.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']

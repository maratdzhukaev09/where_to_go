from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    fields = ['image', 'get_preview', 'number', 'place']
    readonly_fields = ['get_preview']
    extra = 0

    def get_preview(self, image):
        if image.image:
            return format_html('<img src="{}" height=200px />', image.image.url)
        return 'Фотография не добавлена'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
    ordering = ['place__title', 'number']

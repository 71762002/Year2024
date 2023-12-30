from django.contrib import admin

from .models import Holiday, AboutUs, Image


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description",  "created_at")

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "description")



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name")

    
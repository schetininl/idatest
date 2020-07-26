from django.contrib import admin

from .models import Img


class ImageAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "image", "width", "height",) 
    search_fields = ("width", "height") 

admin.site.register(Img, ImageAdmin)

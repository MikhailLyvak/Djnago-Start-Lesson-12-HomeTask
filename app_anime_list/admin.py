from django.contrib import admin
from .models import Anime, AnimeType

class AnimeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Anime)
admin.site.register(AnimeType, AnimeTypeAdmin)


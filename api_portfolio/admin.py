from attr import fields
from django.contrib import admin

from .models import Trabalhos, AudioVisual, Locucao, Produtora, Teatro, Youtube, Director, Album

# Register your models here.
class AlbumInline(admin.TabularInline):
    model = Album
    fields = ['image']

@admin.register(Trabalhos)
class TrabalhosAdmin(admin.ModelAdmin):
    list_display = ['trabalho', 'titulo', 'director', 'video','data', 'ativo' ]
    inlines=[AlbumInline]

# @admin.register(Teatro)
# class TeatroAdmin(admin.ModelAdmin):
#     list_display = ['titulo', 'director', 'video','data', 'ativo' ]
#     inlines=[AlbumInline]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['image']


# @admin.register(AudioVisual)
# class AudioVisualAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Locucao)
# class LocucaoAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Youtube)
# class YoutubeAdmin(admin.ModelAdmin):
#     pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Produtora)
class ProdutoraAdmin(admin.ModelAdmin):
    pass
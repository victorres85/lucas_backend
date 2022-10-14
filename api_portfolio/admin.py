from django.contrib import admin

from .models import AudioVisual, Locucao, Produtora, Teatro, Youtube, Director

# Register your models here.

@admin.register(Teatro)
class TeatroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'director', 'video','data', 'ativo' ]

@admin.register(AudioVisual)
class AudioVisualAdmin(admin.ModelAdmin):
    pass

@admin.register(Locucao)
class LocucaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Youtube)
class YoutubeAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Produtora)
class ProdutoraAdmin(admin.ModelAdmin):
    pass
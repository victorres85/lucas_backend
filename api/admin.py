from django.contrib import admin

from api.models import AudioVisual, Diretor, Locucao, Produtora, Teatro, Youtube

# Register your models here.

@admin.register(Teatro)
class TeatroAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(AudioVisual)
class AudioVisualAdmin(admin.ModelAdmin):
    pass

@admin.register(Locucao)
class LocucaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Youtube)
class YoutubeAdmin(admin.ModelAdmin):
    pass

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    pass

@admin.register(Produtora)
class ProdutoraAdmin(admin.ModelAdmin):
    pass
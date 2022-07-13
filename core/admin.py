from django.contrib import admin
from core.models import Articulos
from core import models

class ArticulosAdmin(admin.ModelAdmin):
    #campos para mostrar en el admin list
    list_display=('nombre','seccion','precio')
    search_fields=('nombre', 'seccion')
    list_filter=['seccion']

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(Articulos, ArticulosAdmin)

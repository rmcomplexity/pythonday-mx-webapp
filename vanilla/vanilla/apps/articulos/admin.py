from django.contrib import admin
from vanilla.apps.articulos.models import Articulo

# Register your models here.
@admin.register(Articulo)
class ArticulosAdmin(admin.ModelAdmin):
    pass

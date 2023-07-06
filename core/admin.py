from django.contrib import admin

from core.models import Menu, Plato, Restaurante


class RestauranteAdmin(admin.ModelAdmin):
    fields = ["nombre", "usuario"]
    list_display = ["id", "nombre", "usuario"]
    search_fields = ["nombre"]


class MenuAdmin(admin.ModelAdmin):
    fields = ["nombre", "restaurante"]
    list_display = ["id", "nombre", "restaurante"]
    search_fields = ["nombre", "restaurante"]


class PlatoAdmin(admin.ModelAdmin):
    fields = ["nombre", "precio", "descripcion"]
    list_display = ["id", "nombre", "menu"]
    search_fields = ["nombre", "menu"]


admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Plato, PlatoAdmin)

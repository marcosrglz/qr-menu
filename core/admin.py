from django.contrib import admin

from core.models import Restaurante


class RestauranteAdmin(admin.ModelAdmin):
    fields = ["nombre", "usuario"]
    list_display = ["id", "nombre", "usuario"]
    search_fields = ["nombre"]


admin.site.register(Restaurante, RestauranteAdmin)

from django.contrib import admin

from core.models import Menu, Plato, Restaurante


class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 0


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0


class RestauranteAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    inlines = [MenuInline]
    list_display = ["id", "nombre", "usuario"]
    search_fields = ["nombre"]


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    inlines = [PlatoInline]
    list_display = ["id", "nombre", "restaurante", "creado", "modificado"]
    search_fields = ["nombre", "restaurante"]


class PlatoAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "menu"]
    search_fields = ["nombre", "menu"]


admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Plato, PlatoAdmin)

from django.contrib import admin

from core.models import Menu, Categoria, Plato


class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 0


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "usuario", "creado", "modificado"]
    search_fields = ["nombre", "usuario"]


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "menu"]
    search_fields = ["nombre", "menu"]


class PlatoAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "categoria"]
    search_fields = ["nombre", "categoria"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)

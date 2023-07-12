from django.contrib import admin

from core.models import Menu, Plato


class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 0


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    inlines = [PlatoInline]
    list_display = ["id", "nombre", "usuario", "creado", "modificado"]
    search_fields = ["nombre", "usuario"]


class PlatoAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "menu"]
    search_fields = ["nombre", "menu"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Plato, PlatoAdmin)

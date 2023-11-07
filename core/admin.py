from django.contrib import admin

from core.models import Acceso, Categoria, Menu, Plato


class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 0


class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "usuario", "estado", "creado", "modificado"]
    list_filter = ["estado"]
    search_fields = ["nombre", "usuario"]


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "menu", "estado"]
    list_filter = ["estado"]
    search_fields = ["nombre", "menu"]


class PlatoAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["id", "nombre", "categoria"]
    search_fields = ["nombre", "categoria"]


class AccesoAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "creado", "modificado"]
    list_display = ["menu", "user_agent", "ip"]
    date_hierarchy = "creado"
    search_fields = ["menu"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Menu, MenuAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Acceso, AccesoAdmin)

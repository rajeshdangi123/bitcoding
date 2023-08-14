from django.contrib import admin
from app1.models.tables import Bom, Disti, Unified


# Register your models here.
# admin.site.register(Bom)
class BomAdmin(admin.ModelAdmin):
    list_display = ("part_number", "quantity")


admin.site.register(Bom, BomAdmin)


class DistiAdmin(admin.ModelAdmin):
    list_display = ("part_number", "quantity")


admin.site.register(Disti, DistiAdmin)


class UnifiedAdmin(admin.ModelAdmin):
    list_display = ("bom_pn", "bom_qty", "disti_pn", "disti_qty", "error_flag")


admin.site.register(Unified, UnifiedAdmin)

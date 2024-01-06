from django.contrib import admin
from .models import Kroy_detail, Kroy, Masterdata
from django.utils.safestring import mark_safe


# Register your models here.

class MasterdataAdmin(admin.ModelAdmin):
    list_display = ("kroy_no","edinitsa", "created", "user")

class KroyAdmin(admin.ModelAdmin):
    list_display = ("kroy_no","name", "ras_tkani", "ras_dublerin", "edinitsa", "description", "created", "is_active",)
    search_fields = ("kroy_no",)
    list_editable = ("is_active",)

class Kroy_detailAdmin(admin.ModelAdmin):
    list_display = ("kroy", "pachka", "razmer", "rost", "stuk", "user" )
    search_fields = ("kroy",)


admin.site.register(Masterdata, MasterdataAdmin)
admin.site.register(Kroy, KroyAdmin)
admin.site.register(Kroy_detail, Kroy_detailAdmin)

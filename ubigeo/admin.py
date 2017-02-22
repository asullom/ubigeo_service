from django.contrib import admin

# Register your models here.
from .models import Ubigeo

# Register your models here.


class UbigeoAdmin(admin.ModelAdmin):

    """docstring for UbigeoAdmin"""

    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 70000


admin.site.register(Ubigeo, UbigeoAdmin)

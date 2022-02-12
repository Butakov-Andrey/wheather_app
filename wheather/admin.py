from django.contrib import admin
from .models import Wheather


class WheatherAdmin(admin.ModelAdmin):

    list_display = ("city", "temperature", "created_at")


admin.site.register(Wheather, WheatherAdmin)

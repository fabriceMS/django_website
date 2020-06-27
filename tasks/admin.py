from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # In order to allow the auto completion (in which field it will be made )
    search_fields = ['title']
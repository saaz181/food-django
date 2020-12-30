from django.contrib import admin
from .models import Food
from tinymce.widgets import TinyMCE
from django.db import models


class FoodAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Name", {"fields": ["food_name"]}),
        ("Price", {"fields": ["food_price"]}),
        ("Slug", {"fields": ["food_slug"]}),
        ("Content", {"fields": ["food_description"]}),
    ]
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE}
    }

admin.site.register(Food, FoodAdmin)

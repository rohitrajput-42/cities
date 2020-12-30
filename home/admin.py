from django.contrib import admin
from .models.cities import Cities

class AdminCities(admin.ModelAdmin):
    list_display = ['title', 'desc']

admin.site.register(Cities, AdminCities)
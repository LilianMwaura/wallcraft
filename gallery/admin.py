from django.contrib import admin
from .models import *
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)
    
admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Image)

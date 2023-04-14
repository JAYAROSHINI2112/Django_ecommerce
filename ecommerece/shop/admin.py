from django.contrib import admin

# Register your models here.
from .models import Catagory,Product

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
    
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product)
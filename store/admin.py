from django.contrib import admin
from . models import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name','price','category','category_id']
    
class AdminCategory(admin.ModelAdmin):
    list_display=['name','id']
    

admin.site.register(Customer)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order)


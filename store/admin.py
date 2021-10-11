from django.contrib import admin
from . models import Product,Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name','price','category','category_id']
    
class AdminCategory(admin.ModelAdmin):
    list_display=['name','id']
    


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)


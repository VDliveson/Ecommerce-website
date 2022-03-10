from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import *

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        
class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'username', 'price','email','address','phone')
    
class AdminProduct(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ['id', 'name','price','category','category_id']
    
class AdminCategory(admin.ModelAdmin):
    list_display=['name','id']
   
class AdminCustomer(ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ['id', 'username','email','password','phone']


    

admin.site.register(Customer,AdminCustomer)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order)
admin.site.register(Vendor)

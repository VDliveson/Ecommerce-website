from django.db import models
from .category import Category
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=9,decimal_places=2,default=0)
    description=models.CharField(max_length=5000,default='')
    image=models.ImageField(upload_to='uploads/products',default='uploads/products/default-store.jpg')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if(category_id):
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
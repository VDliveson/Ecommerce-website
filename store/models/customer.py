from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    address =models.CharField(max_length=512)
    phone=models.CharField(max_length=10)
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_Customer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    
    def is_Exists(self):
        if(Customer.objects.filter(email=self.email)):
            return True
        else:
            return False

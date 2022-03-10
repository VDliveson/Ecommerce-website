from django.db import models

class Vendor(models.Model):
    username = models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_Vendor(email):
        try:
            return Vendor.objects.get(email=email)
        except:
            return False
        
    
    def is_Exists(self):
        if(Vendor.objects.filter(email=self.email)):
            return True
        else:
            return False

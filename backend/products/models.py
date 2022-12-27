from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    user=models.ForeignKey(User,related_name="user_product",on_delete=models.SET_NULL,default=1,null=True)
    title=models.CharField(max_length=255)
    desc=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    public=models.BooleanField(default=True)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)

    def get_discount(self):
        return "this is an instance"
    

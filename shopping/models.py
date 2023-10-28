from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    quantity = models.IntegerField(default=0,blank=False,null=False)
    date = models.DateField(auto_now_add=True,blank=False,null=False)
    cost = models.IntegerField(default=0,blank=False,null=False)

    
    def __str__(self):
        return self.name
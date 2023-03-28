from django.db import models

# Create your models here.
class Item(models.Model):
    # category = models.CharField(max_length=255)
    # subcategory = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    # amount = models.PositiveIntegerField()
    
    
    name = models.CharField(max_length=255)
    roll = models.PositiveIntegerField()
    email = models.EmailField(max_length=255)
    group = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 
    
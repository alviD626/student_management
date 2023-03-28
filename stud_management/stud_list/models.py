from django.db import models

# Create your models here.
class Item(models.Model):
    
    name = models.CharField(max_length=255)
    roll = models.PositiveIntegerField()
    email = models.EmailField(max_length=255)
    group = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 
    
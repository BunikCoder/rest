from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    photo = models.ImageField()
    
    def __str__(self) -> str:
        return self.name
    

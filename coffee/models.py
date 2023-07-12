from django.db import models

class Coffee(models.Model):
    id = models.IntegerField(primary_key =True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="coffee")
    price = models.IntegerField(max_length=10, null=True)
    
    
    def __str__(self):
        return self.name
    
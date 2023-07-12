from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200, db_index=True)
    last_name = models.SlugField(max_length=200, db_index=True)
    adress = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

    
        

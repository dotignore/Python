from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=200)

# Create your models here.
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Order_'
        verbose_name_plural = '_Orders'
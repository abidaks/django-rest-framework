from django.db import models

from insurance.apps.customer.models import Customer

class Policy(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    premium = models.BigIntegerField()
    cover = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name_plural = "Policies"

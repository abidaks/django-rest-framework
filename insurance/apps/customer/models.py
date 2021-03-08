from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

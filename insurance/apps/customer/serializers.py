from rest_framework import serializers 
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    dob = serializers.DateField(input_formats=['%d-%m-%Y',])
 
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob', 'created_on', 'updated_at')
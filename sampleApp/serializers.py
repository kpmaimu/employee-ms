from .models import Employee
# from .models import Employee,Image
from rest_framework import serializers

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         fields=['photo']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['emp_id','emp_name','designation','join_date']

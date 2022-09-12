from django.db import models



class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    join_date=models.DateField(blank=True,default='2020-03-13')
    
# class Image(models.Model):
#     photo=models.ImageField(upload_to='images',blank=True,null=True)
#     employee_id=models.OneToOneField(Employee,on_delete=models.CASCADE,default=3)

class Phone(models.Model):
    phone_no=models.CharField(max_length=10)
    employee_id=models.OneToOneField(Employee,on_delete=models.CASCADE)



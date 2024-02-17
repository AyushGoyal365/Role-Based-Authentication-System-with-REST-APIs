from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

   

    def __str__(self):
        return self.username
    
class Employee(models.Model):
    Employee_id = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=100)
    Employee_email = models.CharField(max_length=100)
    Employee_role = models.CharField(max_length =100,choices =(('Back-end Developer','Back-end Developer'),('front-end Developer','front-end Developer'),('UX/UI Designer','UX/UI Designer'),('Product Manager','Product Manager')))
    Created_at = models.DateTimeField(auto_now = True)




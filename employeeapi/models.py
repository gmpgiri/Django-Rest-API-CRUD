from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=13)

    # Create / Insert / Add - POST
    # Retrive / Fetch / Select- GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
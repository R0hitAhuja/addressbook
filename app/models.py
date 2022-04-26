from django.db import models
import uuid
# Create your models here.


class Employee(models.Model):

    first_name = models.CharField(max_length = 1000)
    last_name = models.CharField(max_length = 1000)
    cust_id = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    age = models.IntegerField()
    sex = models.CharField(max_length = 100)
    address = models.CharField(max_length = 1000)
    contactno = models.CharField(max_length = 1000)

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    name = models.CharField(max_length = 1000)
    author = models.CharField(max_length = 1000)
    price = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

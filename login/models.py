from django.db import models

# # Create your models here.
class User_info(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.fname +" "+ self.lname

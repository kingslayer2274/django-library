from django.db import models

# Create your models here.


class Users(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100)
    role= models.CharField(max_length=2,choices=[("a","admin"),("s","student")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
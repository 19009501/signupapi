from django.db import models

class UserProfile(models.Model):
    name=models.CharField(max_length=200,default=None)
    email=models.EmailField(max_length=30,default=None)
    phone_number=models.CharField(max_length=255,null=False)
    password=models.CharField(max_length=10,default=None,null=True)

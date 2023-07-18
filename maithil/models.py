from django.db import models

# Create your models here.

class Signup(models.Model):
	usename=models.CharField(max_length=200)
	email=models.EmailField()
	password=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	city=models.CharField(max_length=50)
	address=models.TextField()
	zipcode=models.PositiveIntegerField()

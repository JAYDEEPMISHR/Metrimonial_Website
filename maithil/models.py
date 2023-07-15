from django.db import models

# Create your models here.

class Signup(models.Model):
	usename=models.CharField(max_length=200)
	email=moddls.EmailField()
	
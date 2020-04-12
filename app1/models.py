from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	reader = models.ForeignKey(User,on_delete=models.CASCADE)
	title  = models.CharField(max_length=100)
	amazon_url = models.URLField(max_length=200)
	author = models.CharField(max_length=100)
	genre  = models.CharField(max_length=100)

from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.TextField()
	desc  = models.TextField()
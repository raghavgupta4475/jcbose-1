from django.db import models

# Create your models here.

class User(models.Model):
	title = models.TextField()
	desc  = models.TextField()
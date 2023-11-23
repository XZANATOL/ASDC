from django.db import models

class Record(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	location = models.CharField(max_length=70)
	price = models.FloatField()
	color = models.CharField(max_length=15)
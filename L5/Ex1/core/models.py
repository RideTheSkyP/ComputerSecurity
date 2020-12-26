from django.db import models


# Create your models here.
class Transfers(models.Model):
	userId = models.IntegerField()
	transferFrom = models.IntegerField()
	transferTo = models.IntegerField()
	amount = models.FloatField()

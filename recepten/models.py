from __future__ import unicode_literals

from django.db import models


# Create your models here.
class recept(models.Model):
	recept_naam = models.CharField(max_length=50)
	recept_calorie = models.CharField(max_length=500)
    recept_ingredient = models.CharField(max_length=500)
    recept_tijd = models.CharField(max_length=500)

	def __unicode__(self):
		return self.recept_naam

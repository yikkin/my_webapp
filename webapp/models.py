from django.db import models

# Create your models here.

class Technologies(models.Model):
	techno = models.CharField(max_length = 50)

	def __str__(self):
		return self.techno

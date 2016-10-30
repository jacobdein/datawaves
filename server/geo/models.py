from django.contrib.gis.db import models


class Boundary(models.Model):
	name = models.CharField(max_length = 50)
	shape = models.PolygonField(srid = 31254)
	
	def __str__(self):
		return self.name
		
	class Meta():
		verbose_name_plural = 'Boundaries'
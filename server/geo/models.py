from django.contrib.gis.db import models


class Boundary(models.Model):
	name = models.CharField(max_length = 50)
	shape = models.PolygonField(srid = 31254)
	
	def __str__(self):
		return self.name
		
	class Meta():
		verbose_name_plural = 'Boundaries'


class SampleLocation(models.Model):
	probability = models.FloatField(blank = True)
	landcover = models.IntegerField(blank = True)
	naturalness = models.FloatField(blank = True)
	shape = models.PointField(srid = 31254)
	
	def __str__(self):
		return "{0} - land: {1}".format(self.id, self.landcover)

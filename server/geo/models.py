from django.contrib.gis.db import models


class Boundary(models.Model):
	name = models.CharField(max_length = 50)
	geometry = models.PolygonField(srid = 31254)
	
	def __str__(self):
		return self.name
		
	class Meta():
		verbose_name_plural = 'Boundaries'


class SampleLocation(models.Model):
	probability = models.FloatField(blank = True)
	landcover = models.IntegerField(blank = True)
	naturalness = models.FloatField(blank = True)
	geometry = models.PointField(srid = 31254)
	
	def __str__(self):
		return "{0} - land: {1}".format(self.id, self.landcover)


# Too many issues with rasters, revisit
#class Raster(models.Model):
#	name = models.CharField(max_length = 50)
#	raster = models.RasterField(srid = 31254)
#	
#	def __str__(self):
#		return "{0} - {1}".format(self.id, self.name)


class Raster(models.Model):
	name = models.CharField(max_length = 50)
	filepath = models.CharField(max_length = 250)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)
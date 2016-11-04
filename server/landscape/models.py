#from django.db import models
from django.contrib.gis.db import models


class LandCover(models.Model):
	cover_type = models.IntegerField()
	geometry = models.MultiPolygonField(srid = 31254)


class LandCoverArea(models.Model):
	id = models.AutoField(primary_key = True)
	included_area = models.CharField(max_length = 50)
	type_1 = models.FloatField(blank = True)
	type_2 = models.FloatField(blank = True)
	type_3 = models.FloatField(blank = True)
	type_4 = models.FloatField(blank = True)
	type_5 = models.FloatField(blank = True)
	type_6 = models.FloatField(blank = True)
	type_7 = models.FloatField(blank = True)
	type_8 = models.FloatField(blank = True)
	type_9 = models.FloatField(blank = True)
	type_10 = models.FloatField(blank = True)
	type_11 = models.FloatField(blank = True)
	type_12 = models.FloatField(blank = True)
	type_13 = models.FloatField(blank = True)
	type_14 = models.FloatField(blank = True)
	type_15 = models.FloatField(blank = True)
	site = models.ForeignKey('database.Site', on_delete = models.CASCADE, db_column = 'site')
	
	def __str__(self):
		return "{0} - {1}".format(self.site.name, self.included_area)
		

class NaturalnessArea(models.Model):
	id = models.AutoField(primary_key = True)
	included_area = models.CharField(max_length = 50)
	type_1 = models.FloatField(blank = True)
	type_2 = models.FloatField(blank = True)
	type_3 = models.FloatField(blank = True)
	type_4 = models.FloatField(blank = True)
	type_5 = models.FloatField(blank = True)
	type_6 = models.FloatField(blank = True)
	type_7 = models.FloatField(blank = True)
	mean = models.FloatField(blank = True)
	site = models.ForeignKey('database.Site', on_delete = models.CASCADE, db_column = 'site')
	
	def __str__(self):
		return "{0} - {1}".format(self.site.name, self.included_area)
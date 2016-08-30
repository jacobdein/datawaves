from django.db import models


class Record(models.Model):
	id = models.IntegerField(primary_key = True)
	date = models.DateField()
	time = models.TimeField()
	temperature = models.FloatField(blank = True, null = True)
	precipitation = models.FloatField(blank = True, null = True)
	humidity = models.FloatField(blank = True, null = True)
	dew_point = models.FloatField(blank = True, null = True)
	wind_speed = models.FloatField(blank = True, null = True)
	wind_direction = models.FloatField(blank = True, null = True)
	pressure = models.FloatField(blank = True, null = True)
	site = models.ForeignKey('Site', on_delete = models.CASCADE, db_column = 'site')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.date)


class Site(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50, blank = True)
	lat = models.FloatField(blank = True, null = True)
	lon = models.FloatField(blank = True, null = True)
	elevation = models.FloatField(blank = True, null = True)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)
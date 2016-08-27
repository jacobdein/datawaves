from django.db import models


class Sound(models.Model):
	sound_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	site_id = models.ForeignKey('Site', on_delete = models.CASCADE, db_column = 'site_id')
	collection_id = models.ForeignKey('Collection', on_delete = models.CASCADE, db_column = 'collection_id')
	sensor_id = models.ForeignKey('Sensor', on_delete = models.CASCADE, db_column = 'sensor_id')
	date = models.DateField()
	time = models.TimeField()
	quality = models.IntegerField(blank = True)
	notes = models.TextField(blank = True)
	filepath = models.CharField(max_length = 1000)
	MD5_hash = models.CharField(max_length = 32, blank = True)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.name, self.site_id)


class Site(models.Model):
	site_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	lat = models.FloatField(blank = True)
	lon = models.FloatField(blank = True)
	elevation = models.FloatField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.site_id, self.name)


class Collection(models.Model):
	collection_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	created_by = models.CharField(max_length = 50, blank = True)
	source_type = models.CharField(max_length = 50, blank = True)
	citation = models.TextField(blank = True)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.collection_id, self.name)


class Sensor(models.Model):
	sensor_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	microphone = models.CharField(max_length = 250, blank = True)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.sensor_id, self.name)
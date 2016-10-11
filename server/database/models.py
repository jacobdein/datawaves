from django.db import models
from datawaves import settings
import os.path


class Setting(models.Model):
	sound_directory = models.CharField(max_length = 1000, blank = True)
	sound_preview_directory = models.CharField(max_length = 1000, blank = True)
	spectrogram_image_directory = models.CharField(max_length = 1000, blank = True)
	
	def __str__(self):
		return "settings"


class Sound(models.Model):
	
	QUALITY_CHOICES = (
		(0, 'none'),
		(1, 'one'),
		(2, 'two'),
		(3, 'three'),
	)
	
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	site = models.ForeignKey('Site', on_delete = models.CASCADE, db_column = 'site')
	collection = models.ForeignKey('Collection', on_delete = models.CASCADE, db_column = 'collection')
	sensor = models.ForeignKey('Sensor', on_delete = models.CASCADE, db_column = 'sensor')
	date = models.DateField()
	time = models.TimeField()
	quality = models.IntegerField(blank = True, choices = QUALITY_CHOICES, default = 0)
	notes = models.TextField(blank = True)
	custom_filepath = models.CharField(max_length = 1000)
	MD5_hash = models.CharField(max_length = 32, blank = True)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.name, self.id)
	
	# update when .flac storage is implemented
	def get_filepath(self):
		return os.path.join(settings.STATICFILES_DIRS[1], Setting.objects.get(id = 1).sound_directory, 
							str(self.collection.id), str(self.site.id), self.name + '.wav')


class Site(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	lat = models.FloatField(blank = True)
	lon = models.FloatField(blank = True)
	elevation = models.FloatField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)


class Collection(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	created_by = models.CharField(max_length = 50, blank = True)
	source_type = models.CharField(max_length = 50, blank = True)
	citation = models.TextField(blank = True)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)


class Sensor(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	microphone = models.CharField(max_length = 250, blank = True)
	notes = models.TextField(blank = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)
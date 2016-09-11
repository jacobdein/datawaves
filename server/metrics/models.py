from django.db import models


class SoundscapeSpec(models.Model):
	id = models.IntegerField(primary_key = True)
	frequency_power = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	call = models.ForeignKey('Call', on_delete = models.SET_NULL, null = True, db_column = 'call')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)


class Call(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	language = models.CharField(max_length = 50)
	call = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)
from django.db import models


class NDSI(models.Model):
	id = models.AutoField(primary_key = True)
	ndsi_left = models.FloatField()
	ndsi_right = models.FloatField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)
	
	class Meta():
		verbose_name = 'NDSI'
		verbose_name_plural = 'NDSIs'


class BioacousticIndex(models.Model):
	id = models.AutoField(primary_key = True)
	bai_left = models.FloatField()
	bai_right = models.FloatField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)
	
	class Meta():
		verbose_name_plural = 'bioacoustic complexity indices'


class AcousticComplexityIndex(models.Model):
	id = models.AutoField(primary_key = True)
	aci_left = models.FloatField()
	aci_right = models.FloatField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)
	
	class Meta():
		verbose_name_plural = 'acoustic complexity indices'


class SoundscapeSpec(models.Model):
	id = models.AutoField(primary_key = True)
	frequency_power = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)


class SoundExposureLevel(models.Model):
	id = models.AutoField(primary_key = True)
	sel = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)


class PowerSpectrumSum(models.Model):
	id = models.AutoField(primary_key = True)
	anthrophony = models.FloatField()
	biophony = models.FloatField()
	total = models.FloatField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	sound = models.ForeignKey('database.Sound', on_delete = models.CASCADE, db_column = 'sound')
	analysis = models.ForeignKey('Analysis', on_delete = models.SET_NULL, null = True, db_column = 'analysis')
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.sound.name)


class Analysis(models.Model):
	
	class Meta:
		verbose_name_plural = 'analyses'
	
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	language = models.CharField(max_length = 50)
	call = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return "{0} - {1}".format(self.id, self.name)

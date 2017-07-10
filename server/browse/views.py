from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Avg

from database.models import Sound, Setting
from weather.models import Record
from metrics.models import SoundExposureLevelAdvanced
from .forms import QualityForm

from datetime import date, time, timedelta, datetime
import numpy as np
import os.path


def index(request):
	n_sounds = Sound.objects.count()
	return HttpResponse("There are {0} sounds in the database".format(n_sounds))


def sound(request, id):
	sound = get_object_or_404(Sound, pk = id)
	if sound.custom_filepath != '':
		path = sound.custom_filepath
	else:
		path = os.path.join(settings.STATIC_URL, Setting.objects.get(id = 1).sound_directory, str(sound.collection.id), str(sound.site.id), sound.name + ".flac")
	sound_preview = os.path.join(settings.STATIC_URL, Setting.objects.get(id = 1).sound_preview_directory, str(sound.collection.id), str(sound.site.id), sound.notes)
	spectrogram_image = os.path.join(settings.STATIC_URL, Setting.objects.get(id = 1).spectrogram_image_directory, str(sound.collection.id), str(sound.site.id), str(sound.name) + ".png")
	spectrogram_image_ale = os.path.join(settings.STATIC_URL, Setting.objects.get(id = 1).spectrogram_image_directory, 'ale2', str(sound.collection.id), str(sound.site.id), str(sound.name) + ".png")
	
	# weather data
	time_offset = timedelta(hours = 1)
	recorded_datetime = datetime(sound.date.year, sound.date.month, sound.date.day, sound.time.hour, sound.time.minute, sound.time.second)
	
	start_offset = recorded_datetime - time_offset
	end_offset = recorded_datetime + time_offset
	
	temperature = "{0:.1f}".format(Record.objects.filter(date__range = (start_offset.date(), end_offset.date()), time__range = (start_offset.time(), end_offset.time())).aggregate(Avg('temperature'))['temperature__avg'])
	
	wind_speed = "{0:.1f}".format(Record.objects.filter(date__range = (start_offset.date(), end_offset.date()), time__range = (start_offset.time(), end_offset.time())).aggregate(Avg('wind_speed'))['wind_speed__avg'])
	
	# metrics
	sel_record = SoundExposureLevelAdvanced.objects.get(sound = sound.id)
	anthrophony = "{0:.4f}".format(sel_record.anthrophony)
	biophony = "{0:.4f}".format(sel_record.biophony)
	
	#anthrophony = spec[0:2].sum()
	#biophony = spec[2:8].sum()
	
	context = {
		'sound': sound, 
		'path': path, 
		'sound_preview': sound_preview, 
		'spectrogram_image': spectrogram_image, 
		'spectrogram_image_ale': spectrogram_image_ale, 
		'temperature': temperature, 
		'wind_speed': wind_speed, 
		'anthrophony': anthrophony, 
		'biophony': biophony,
	}
	
	# render quality form 
	if request.method == 'POST':
		quality_form = QualityForm(request.POST)
		if quality_form.is_valid():
			quality = int(quality_form.cleaned_data['quality'])
			sound.quality = quality
			sound.save()
			quality_name = [ c[1] for c in Sound.QUALITY_CHOICES if c[0] == quality ][0]
			context['quality_form_message'] = "quality updated to '{0}'".format(quality_name)
	quality_form = QualityForm(initial = {'quality': "{0}".format(sound.quality)})
	context['quality_form'] = quality_form
	
	return render(request, 'sound.html', context = context)

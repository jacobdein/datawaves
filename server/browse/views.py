from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from database.models import Sound, Setting
from django.conf import settings

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
	spectrogram_image = os.path.join(settings.STATIC_URL, Setting.objects.get(id = 1).spectrogram_image_directory, str(sound.collection.id), str(sound.site.id), str(sound.id) + "-large_s.png")
	return render(request, 'sound.html', {'sound': sound, 'path': path, 'sound_preview': sound_preview, 'spectrogram_image': spectrogram_image})

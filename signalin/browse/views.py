from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from database.models import Sound


def index(request):
	n_sounds = Sound.objects.count()
	return HttpResponse("There are {0} sounds in the database".format(n_sounds))


def sound(request, id):
	sound = get_object_or_404(Sound, pk = id)
	return render(request, 'sound.html', {'sound': sound})

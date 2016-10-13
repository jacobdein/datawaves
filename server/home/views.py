from django.shortcuts import render
from database.models import Sound

def home(request):
	n_sounds = Sound.objects.count()
	return render(request, 'index.html', {'n_sounds':n_sounds})
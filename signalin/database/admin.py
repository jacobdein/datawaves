from django.contrib import admin

from .models import Sound, Site, Collection, Sensor

admin.site.register(Sound)
admin.site.register(Site)
admin.site.register(Collection)
admin.site.register(Sensor)
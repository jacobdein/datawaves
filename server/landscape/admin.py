from django.contrib.gis import admin

# Register your models here.
from .models import LandCover, LandCoverArea, NaturalnessArea
admin.site.register(LandCover, admin.OSMGeoAdmin)
admin.site.register(LandCoverArea)
admin.site.register(NaturalnessArea)
from django.contrib import admin

from .models import SoundscapeSpec, SoundExposureLevel, Analysis
admin.site.register(SoundscapeSpec)
admin.site.register(SoundExposureLevel)
admin.site.register(Analysis)
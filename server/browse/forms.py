from django import forms
from database.models import Sound


class QualityForm(forms.Form):
	quality = forms.ChoiceField(label = 'quality', choices = Sound.QUALITY_CHOICES)
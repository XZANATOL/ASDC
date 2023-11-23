from django import forms
from . import models

class RecordForm(forms.ModelForm):
	class Meta:
		model = models.Record
		fields = ("name", "description", "location", "price", "color")
		
from django import forms
from . models import Technologies

class TechnologiesForm(forms.ModelForm):
    class Meta:
        model = Technologies
        fields = ["techno"]
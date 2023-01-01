from django import forms
from .models import Rider, Requester

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name', 'from_location', 'to_location', 'assets']

class RequesterForm(forms.ModelForm):
    class Meta:
        model = Requester
        fields = ['name', 'from_location', 'to_location', 'asset_type', 'assets']

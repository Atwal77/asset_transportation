from django import forms
from .models import Rider, Requester, TransportationRequest

# Define constants for valid asset types and sensitivities
VALID_ASSET_TYPES = ['LAPTOP', 'TRAVEL_BAG', 'PACKAGE']
VALID_SENSITIVITIES = ['HIGHLY_SENSITIVE', 'SENSITIVE', 'NORMAL']


class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name', 'from_location', 'to_location', 'assets']

class RequesterForm(forms.ModelForm):
    class Meta:
        model = Requester
        fields = ['name', 'email_id', 'from_location', 'to_location', 'asset_type', 'assets']


class TransportationRequestForm(forms.ModelForm):
    class Meta:
        model = TransportationRequest
        fields = ['from_location', 'to_location', 'asset_type', 'num_assets', 'sensitivity']

    def clean(self):
        cleaned_data = super().clean()
        asset_type = cleaned_data.get('asset_type')
        sensitivity = cleaned_data.get('sensitivity')

        if asset_type not in VALID_ASSET_TYPES:
            raise forms.ValidationError("Invalid asset type")
        if sensitivity not in VALID_SENSITIVITIES:
            raise forms.ValidationError("Invalid sensitivity")

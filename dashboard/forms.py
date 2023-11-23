from django import forms
from .models import emailMarketing

class EmailMarketingForm(forms.ModelForm):
    class Meta:
        model = emailMarketing
        fields = ['email']

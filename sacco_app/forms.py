# forms.py
from django import forms
from .models import CreditRiskInput

class CreditRiskForm(forms.ModelForm):
    class Meta:
        model = CreditRiskInput
        fields = '__all__'


"""Forms for the tasks app."""
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(label="name")
    description = forms.Textarea()
    quantity = forms.NumberInput()

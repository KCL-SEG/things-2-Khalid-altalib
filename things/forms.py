"""Forms of the project."""
"""The project includes a nearly empty file called things/forms.py. 
In this file, define a form called ThingForm, that contains the fields name, description, and quantity, 
but not created_at.

The form must accept valid inputs for Thing and reject invalid input for Thing.

The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput"""
# Create your forms here.

from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.ModelForm):

    """
    name = forms.CharField(max_length=35, unique=True)
    description = forms.CharField(max_length=120, blank=True)
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    """
    class Meta:
        # The form must accept valid inputs for Thing and reject invalid input for Thing.

        model = Thing
        # The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput
        fields = ['name', 'description', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'quantity': forms.NumberInput(attrs={'min': 0}),
        }

from django import forms
from .models import Something

class Valueform(forms.ModelForm):
    class Meta:
        model = Something
        
        fields =[
            'name',
            'age',
            'email',
            'description',
            'height',
            'some_image'
        ]
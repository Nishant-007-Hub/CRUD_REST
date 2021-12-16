from django import forms
from .models import*

class SingerAdd(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['name', 'gender']
        # below widgets are use for manually configure default ModelForm design like bootstrape
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'gender' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
         }
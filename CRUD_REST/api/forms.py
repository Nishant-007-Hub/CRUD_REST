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
            # if password is your field and u want to show it to frontend than chk below
            # 'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control form-control-sm'}), # default render_value is False

         }
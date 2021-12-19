from django import forms
from django.forms.models import ModelChoiceField
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

class SongAdd(forms.ModelForm):
    # below line is specially use for foreignkey in modelform like show dropdown of foreignkey in frontend
    singer = ModelChoiceField(queryset=Singer.objects.all())
    class Meta:
        model = Song
        # fields = ['title','duration']
        fields = '__all__'
        # below widgets are use for manually configure default ModelForm design like bootstrape
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'singer' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'duration' : forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            # if password is your field and u want to show it to frontend than chk below
            # 'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control form-control-sm'}), # default render_value is False

         }


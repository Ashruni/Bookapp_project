from django import forms
from .models import*
from django.contrib.auth.models import  User
from django.contrib.auth.models import User
class regforms(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password']

class logform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50)

class uploadform(forms.ModelForm):
    class Meta:
        model = uploaddisplaym
        fields='__all__'
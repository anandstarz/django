from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class loginform(ModelForm):
    class Meta:
	model = User
	fields = ('username', 'email', 'password')
	widgets={

            "username":forms.TextInput(attrs={'placeholder':'Name','class':'textBox','id':'first_name'}),
            "email":forms.TextInput(attrs={'placeholder':'Email','class':'textBox','id':'email','type':'email'}),
            "password":forms.TextInput(attrs={'placeholder':'Password','class':'textBox','id':'password', 'type':'password'}),

                  }



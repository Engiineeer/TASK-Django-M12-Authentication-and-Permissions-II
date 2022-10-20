from pickle import TRUE
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        field = ["username","password"]
        widgets = {
            "password" : forms.PasswordInput()
        }


class UserSigninForm(forms.Form):
    username = forms.CharField(required=TRUE)
    password = forms.CharField(required=TRUE, widget=forms.PasswordInput())
    

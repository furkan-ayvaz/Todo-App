from django import forms
from django.contrib.auth.models import User


class Register(forms.Form):
    username = forms.CharField(max_length = 50, label = "Username")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    confirm = forms.CharField(label = "Confirm your password", widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm") 
        if User.objects.filter(username = username):
            raise forms.ValidationError("This username is already taken")   
        if (password and confirm) and (password == confirm):   
            values = {
                "username":username,
                "password":password,
            }
            return values
        else:
            raise forms.ValidationError("Passwords do not match !!!")


class Login(forms.Form):
    username = forms.CharField(max_length=50,label = "Username")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)


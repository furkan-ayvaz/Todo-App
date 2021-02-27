from django import forms
from .models import TODO


class todo_form(forms.ModelForm):
    class Meta:
        fields = ["todo_describe","todo_case"]
        model = TODO
        

from django import forms
from .models import products1

class products1(forms.ModelForm):
    class Meta:
        model = products1
        fields = ['fname','lname','username','email','password']
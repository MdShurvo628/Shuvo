from django import forms
from .models import User_info

class UserEntry(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ['fname','lname','username','email','password']
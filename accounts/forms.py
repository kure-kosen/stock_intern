from django import forms
from .models import User

class UserForm(forms.ModelForm):
    user_id = forms.CharField()
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("user_id", "user_name", "password")

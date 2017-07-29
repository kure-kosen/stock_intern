from django import forms

class UserForm(forms.Form):
    user_id = forms.CharField()
    user_name = forms.CharField()
    password = forms.CharField()

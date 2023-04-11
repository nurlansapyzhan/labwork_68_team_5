from django import forms
from django.contrib.auth import get_user_model



class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Электронная почта или телефон'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'login_input'})
    password.widget.attrs.update({'class': 'login_input mt-2'})




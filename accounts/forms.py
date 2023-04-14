from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

CHOICE_ROLE = [
    ('True', 'Я соикатель'),
    ('False', 'Я работодатель')
]

def validate_digits(value):
    if not value.isdigit():
        raise ValidationError('Phone number should contain only digits')


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Электронная почта или телефон'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'login_input'})
    password.widget.attrs.update({'class': 'login_input mt-2'})


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label='', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(label='', strip=False, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_confirm = forms.CharField(label='', strip=False, required=True,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    avatar = forms.ImageField(required=False)
    is_applicant = forms.CharField(required=True, widget=forms.RadioSelect(choices=CHOICE_ROLE), label='')
    phone_number = forms.CharField(max_length=11,
                                   validators=[MinLengthValidator(11), validate_digits],
                                   widget=forms.TextInput(attrs={'placeholder': "Номер телефона"}),
                                   label='')

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'password', 'password_confirm', 'avatar', 'is_applicant', 'phone_number'
        )
        labels = {
            'avatar': 'Аватар'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if self.cleaned_data['avatar']:
            user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
        return user

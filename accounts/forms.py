from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from accounts.models import ApplicantProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Электронная почта или телефон'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'login_input'})
    password.widget.attrs.update({'class': 'login_input mt-2'})

class CustomApplicantCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    email = forms.CharField(
        label='Электронная почта',
        required=True,
        widget=forms.TextInput()
    )
    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput()
    )
    phone = forms.IntegerField(
        label='Телефон',
        required=False
    )
    birth_date = forms.DateField(
        label='Дата рождения',
        required=False
    )
    avatar = forms.ImageField(
        label='Аватар',
        required=False,
    )
    location = forms.CharField(
        label='Местоположения',
        required=False,
        widget=forms.TextInput()
    )
    sex = forms.CharField(
        label='Пол',
        widget=forms.Select(),
        required=False
    )
    citizenship = forms.CharField(
        label='Гражданство',
        required=False,
        widget=forms.TextInput()
    )
    bio = forms.CharField(
        label='Биография',
        widget=forms.TextInput(),
        required=False
    )
    has_experience = forms.BooleanField(
        label='Наличие опыта',
        required=False
    )
    experience_year = forms.FloatField(
        label='Годы опыта',
        required=False
    )
    has_driving_lis = forms.BooleanField(
        label='Наличие водительского права',
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'password',
                  'password_confirm', 'first_name',
                  'last_name', 'email',
                  'phone', 'birth_date', 'location',
                  'sex', 'citizenship', 'has_experience',
                  'experience_year', 'has_driving_lis',
                  'bio', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            ApplicantProfile.objects.get_or_create(user=user)
        return user
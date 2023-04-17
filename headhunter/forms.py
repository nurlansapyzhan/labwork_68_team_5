from django import forms
from django.core.exceptions import ValidationError

from .models import Resume, SocialMedia


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            'category', 'name', 'salary',
            'soc_media_link', 'has_experience',
            'experience_year', 'position',
            'responsibility'
        )
        labels = {
            'category': 'Категория',
            'name': 'Наименования резюме',
            'salary': 'Заработная плата',
            'has_experience': 'Наличие опыта',
            'experience_year': 'Годы опыта',
            'position': 'Должность',
            'responsibility': 'Обязанности',
            'soc_media_link': 'Ссылка на соц. сети',
        }

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['name']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data


class SocialMediaForm(forms.ModelForm):
    model = SocialMedia
    fields = ('link')
    labels = {
        'link': 'Ссылка на соц. сети'
    }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='')

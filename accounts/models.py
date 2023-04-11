from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import TextChoices


class SexChoice(TextChoices):
    MALE = ('Male', 'Мужской')
    FEMALE = ('Female', 'Женский')


def validate_digits(value):
    if not value.isdigit():
        raise ValidationError('Phone number should contain only digits')


class Account(AbstractUser):
    username = models.CharField(max_length=30, null=False, unique=True, verbose_name='Username')
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True, null=False)
    phone_number = models.CharField(
        max_length=11,
        verbose_name='Номер телефона',
        unique=True,
        null=False,
        validators=[MinLengthValidator(11), validate_digits],
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='avatars/no_image.png'
    )
    is_applicant = models.BooleanField(verbose_name='Является соискателем')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

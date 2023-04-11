from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class SexChoice(TextChoices):
    MALE = ('Male', 'Мужской')
    FEMALE = ('Female', 'Женский')

class ApplicantProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль заявителя'
    )
    phone = models.IntegerField(
        null=True,
        verbose_name='Телефон номера'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    location = models.TextField(
        max_length=300,
        null=True,
        verbose_name='Местоположение соискателя')
    sex = models.CharField(
        max_length=100,
        null=True,
        choices=SexChoice.choices,
        verbose_name='Пол',
        default=SexChoice.MALE
    )
    citizenship = models.TextField(
        max_length=300,
        null=True,
        verbose_name='Гражданство')
    has_experience = models.BooleanField(
        verbose_name='Наличие опыта',
        null=True,
        default=False)
    experience_year = models.FloatField(
        verbose_name='Годы опыта'
    )
    has_driving_lis = models.BooleanField(
        verbose_name='Наличие водительского права',
        null=True,
        default=False)

    bio = models.TextField(
        max_length=3000,
        null=True,
        verbose_name='Биография пользователя'
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_picture',
        verbose_name='Аватар'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=True,
        default=False)
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user}, {self.phone}"

    class Meta:
        verbose_name = 'Профиль соискателя'
        verbose_name_plural = 'Профили соискателей'

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='employer_profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль работадателя'
    )
    name = models.TextField(
        max_length=300,
        null=False,
        verbose_name='Наименование компании'
    )
    specialization = models.TextField(
        max_length=1000,
        null=True,
        verbose_name='Специализация компании'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        verbose_name='Описание компании'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=True,
        default=False)
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()



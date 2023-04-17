from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class CategoryChoice(TextChoices):
    DESIGN = 'Design', 'Дизайн'
    GAME_DEV = 'Game develope', 'Разработка игр'
    DEVELOPER = 'Develope', 'Разработка'
    TESTING = 'Testing', 'Тестирование'
    HR = 'HR', 'HR'
    OTHER = 'Other', 'Разное'


class Resume(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE,
        primary_key=True
    )
    category = models.CharField(
        verbose_name='Категория резюме',
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Наименование резюме"
    )
    salary = models.PositiveIntegerField(
        verbose_name='Зарплата',
        null=True,
    )
    has_experience = models.BooleanField(
        verbose_name='Наличие опыта',
        null=True,
        default=False
    )
    experience_year = models.FloatField(
        verbose_name='Годы опыта',
        null=True,
    )
    position = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Должность"
    )
    responsibility = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Обязанности"
    )
    is_published = models.BooleanField(
        verbose_name='опубликовано',
        null=False,
        default=False
    )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.category} - {self.name}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

from django.db import models

from headhunter.models import Resume


class SocialMedia(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE
    )
    link = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Ссылки на социальные сети"
    )

    def __str__(self):
        return f'{self.link}'

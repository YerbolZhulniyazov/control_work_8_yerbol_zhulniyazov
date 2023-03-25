from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Review(models.Model):
    author = models.ForeignKey(
        to=User,
        related_name='reviews',
        verbose_name='Автор',
        null=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='webapp.Product',
        verbose_name='Товар',
        related_name='reviews',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name='Текст отзыва',
        null=False,
        blank=False,
        max_length=2500
    )
    grade = models.IntegerField(
        verbose_name="Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True
    )

    def __str__(self):
        return f"{self.author} - {self.product}- {self.description}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    ELECTRONICS = 'Electronics', 'Электроника'
    CARS = 'Cars', 'Машины'
    OTHER = 'Other', 'Разное'


class Product(models.Model):
    name = models.CharField(
        verbose_name='Товар',
        max_length=50,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name="Категория",
        choices=CategoryChoices.choices,
        max_length=50,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=2500,
        null=False,
        blank=False
    )
    image = models.ImageField(
        verbose_name='Картинка',
        null=True,
        blank=True,
        upload_to='image'
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
        return f"{self.name} - {self.category}- {self.description}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

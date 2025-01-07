from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars', verbose_name='Владелец')

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Comment(models.Model):
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments', verbose_name='Автомобиль')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')

    def __str__(self):
        return f"Комментарий от {self.author} к {self.car}"
    
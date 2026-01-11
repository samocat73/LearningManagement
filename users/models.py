from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Укажите город",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="payment")
    payment_dates = models.DateField(
        verbose_name="Дата оплаты", help_text="Укажите дату оплаты"
    )
    course = models.ForeignKey(
        to=Course, on_delete=models.SET_NULL, related_name="payment", null=True
    )
    lesson = models.ForeignKey(
        to=Lesson, on_delete=models.SET_NULL, related_name="payment", null=True
    )
    amount = models.IntegerField(
        verbose_name="Сумма платежа", help_text="Укажите сумму платежа"
    )
    payment_method = models.CharField(
        verbose_name="Способ оплаты", help_text="Укажите способ оплаты"
    )

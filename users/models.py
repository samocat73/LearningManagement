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
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="payment",
        blank=True,
        null=True,
    )
    payment_dates = models.DateField(
        verbose_name="Дата оплаты",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        to=Course, on_delete=models.SET_NULL, related_name="payment", null=True
    )
    lesson = models.ForeignKey(
        to=Lesson, on_delete=models.SET_NULL, related_name="payment", null=True
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма платежа",
    )
    session_id = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        help_text="ID сессии",
    )
    payment_method = models.CharField(
        verbose_name="Способ оплаты", null=True, blank=True
    )
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
    )


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    course = models.ForeignKey(
        to=Course, on_delete=models.CASCADE, related_name="subscriptions"
    )

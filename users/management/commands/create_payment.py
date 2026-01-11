from django.core.management import BaseCommand
from django.utils import timezone

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="example@email.com",
            username="User",
            phone_number="79997845127",
            city="Moscow",
        )
        user.set_password("1234")
        user.is_active = True
        user.save()
        course = Course.objects.create(
            title="Курс игры на гитаре.",
            description="Научу вас играть на гитаре у костра.",
        )
        course.save()
        lesson = Lesson.objects.create(
            title="Урок 1.",
            description="На этом уроке у научу вас разбираться в гитарах.",
            course=course,
        )
        current_time = timezone.localtime().date()
        payment = Payment.objects.create(
            user=user,
            payment_dates=current_time,
            course=course,
            lesson=lesson,
            amount=50000,
            payment_method="Наличные",
        )
        payment.save()

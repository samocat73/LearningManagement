from rest_framework import serializers

from users.models import Subscription

from .models import Course, Lesson
from .validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        link = serializers.URLField(validators=[validate_link])
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription_flag = serializers.SerializerMethodField()

    def get_subscription_flag(self, course):
        if Subscription.objects.filter(course=course).exists():
            return "Подписан"
        else:
            return "Не подписан"

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "preview",
            "description",
            "lessons",
            "lesson_count",
            "owner",
            "subscription_flag",
        ]

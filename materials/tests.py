import io

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="user_test@gmail.com",
            phone_number="89587845214",
            city="Moscow",
            username="user_test",
        )
        self.course = Course.objects.create(
            title="Курс по написарию тестов для API.",
            description="Научу вас писать тесты для сервисов API, но это не точно.",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_create(self):
        url = reverse("materials:course-list")
        image = Image.new("RGB", (100, 100))
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")

        file = SimpleUploadedFile(
            name="test.jpg", content=buffer.getvalue(), content_type="image/jpeg"
        )

        data = {
            "title": "Курс по Django.",
            "description": "Курс по Django для чайников.",
            "preview": file,
            "owner": 1,
        }
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {"title": "Курс по написарию тестов для API для чайников!"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), response.data.get("title"))

    def test_destroy(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CourseTestCasePermissions(APITestCase):
    def setUp(self):
        self.user_owner = User.objects.create(
            email="user_test@gmail.com",
            phone_number="89587845214",
            city="Moscow",
            username="user_test",
        )
        self.user_alien = User.objects.create(
            email="user_test_alien@gmail.com",
            phone_number="89587845214",
            city="Moscow",
            username="user_test_alien",
        )
        self.course = Course.objects.create(
            title="Курс по написарию тестов для API.",
            description="Научу вас писать тесты для сервисов API, но это не точно.",
            owner=self.user_owner,
        )
        self.client.force_authenticate(user=self.user_alien)

    def test_list(self):
        url = reverse("materials:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {"title": "Курс по написарию тестов для API для чайников!"}
        response = self.client.patch(url, data)
        print(response.json())
        print(self.user_alien.pk, "Чужак")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

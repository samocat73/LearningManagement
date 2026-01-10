from django.urls import path
from rest_framework import routers

from materials import views
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = routers.SimpleRouter()
router.register("course", views.CourseViewSet)

urlpatterns = [
    path("lesson/", views.LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/create/", views.LessonCreateAPIView.as_view(), name="lesson-create"),
    path(
        "lesson/<int:pk>/", views.LessonRetrieveAPIView.as_view(), name="lesson-detail"
    ),
    path(
        "lesson/<int:pk>/delete/",
        views.LessonDestroyAPIView.as_view(),
        name="lesson-delete",
    ),
    path(
        "lesson/<int:pk>/update/",
        views.LessonUpdateAPIView.as_view(),
        name="lesson-update",
    ),
]
urlpatterns += router.urls

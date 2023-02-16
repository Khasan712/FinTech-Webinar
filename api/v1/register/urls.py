from django.urls import path
from api.v1.register.views import RegisterApi, CourseRegisterApi


urlpatterns = [
    path('', RegisterApi.as_view()),
    path('course/', CourseRegisterApi.as_view()),
]

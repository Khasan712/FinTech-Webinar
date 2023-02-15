from django.urls import path
from api.v1.register.views import RegisterApi


urlpatterns = [
    path('', RegisterApi.as_view()),
]

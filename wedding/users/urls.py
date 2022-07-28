from django.urls import path
from . import views
from .views import UserAPIView


urlpatterns = [
    # path('', views.registration, name='register'),
    path('api/userlist/', views.UserAPIView.as_view()),
]

from django.urls import path
from .views import welcome_index

urlpatterns = [
    path('', welcome_index, name='welcome_home'),
]
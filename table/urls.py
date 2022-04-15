from django.urls import path
from .views import TablePage


urlpatterns = [
    path('', TablePage.as_view(), name='index'),
]
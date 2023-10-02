from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_and_save, name='scrape_and_save'),
]

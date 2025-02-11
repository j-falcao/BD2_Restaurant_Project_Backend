from django.urls import path
from . import views

urlpatterns = [
    path('percentagem_tipos/', views.percentagem_tipos),
]
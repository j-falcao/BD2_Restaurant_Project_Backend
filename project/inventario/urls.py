from django.urls import path
from . import views

urlpatterns = [
    path('ingredientes/', views.ingredientes_view),
]

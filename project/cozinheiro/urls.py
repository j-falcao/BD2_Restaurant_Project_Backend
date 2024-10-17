from django.urls import path, include

urlpatterns = [
    path('pedidos/', include('pedidos.urls')),
    # ...
]
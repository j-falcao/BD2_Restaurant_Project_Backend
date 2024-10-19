from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),
    path('inventario/', include('inventario.urls')),
    path('estatisticas/', include('estatisticas.urls')),
]

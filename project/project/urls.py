from django.urls import path, include

urlpatterns = [
    path('cozinheiro/', include('cozinheiro.urls')),
    path('garcom/', include('garcom.urls')),
    path('produtos/', include('produtos.urls')),
    path('inventario/', include('inventario.urls')),
    path('estatisticas/', include('estatisticas.urls')),
]

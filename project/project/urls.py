from django.urls import path, include

urlpatterns = [
    path('auth/', include('autenticacao.urls')),
    path('servicos/', include('servicos.urls')),
    path('produtos/', include('produtos.urls')),
    path('inventario/', include('inventario.urls')),
    path('estatisticas/', include('estatisticas.urls')),
]

from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from calculator import views

urlpatterns = [
    path('', views.lumens_calculator, name='index'),
    path('api/calculate/', views.LumenCalculatorAPIView.as_view(), name='api-calculate-lumens'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
from django.urls import path
from myapp import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sentimientos API",
        default_version='v1',
        description="API para clasificar sentimientos en comentarios de restaurantes",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'predecir/', views.predecir, name='predecir'),
    path(r'predecirIOJson/', views.predecirIOJson, name='predecirIOJson'),
    path(r'preguntas/', views.preguntas, name='preguntas'),
    path(r'sobre/', views.sobre, name='sobre'),
    path(r'', views.home, name='home'),
]

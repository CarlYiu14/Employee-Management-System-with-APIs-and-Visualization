from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static 
from django.shortcuts import redirect


schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="API documentation for Glynac Internship Project",
      contact=openapi.Contact(email="carlyiu14@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/token/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('django.contrib.auth.urls')),  # enable Django login system
    path('dashboard/', include('dashboard.urls')),
    path('', lambda request: redirect('/swagger/', permanent=False)),  # redirect homepage
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Lead Management API",
        default_version='v1',
        description="APIs for managing leads, stages, and activities",
        contact=openapi.Contact(email="support@pp.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('lead/admin/', admin.site.urls),
    path('lead/api/', include('leads.urls')),
    path('lead/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

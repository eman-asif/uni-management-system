from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponse
from .views import ProtectedView

# ✅ Swagger schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="University Management API",
        default_version='v1',
        description="API documentation for all modules",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ✅ Simple home view
def home(request):
    return HttpResponse("Welcome to UMS!")

urlpatterns = [
    # Home & Admin
    path('', home, name="home"),
    path('admin/', admin.site.urls),

    # Auth (session-based for DRF browsable API)
    path('api-auth/', include('rest_framework.urls')),

    # JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Example protected endpoint
    path("protected/", ProtectedView.as_view(), name="protected"),

    # App routes
    path('api/accounts/', include('accounts.urls')),
    path('api/students/', include('students.urls')),
    path('api/faculty/', include('faculty.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/analytics/', include('analytics.urls')),

    # Swagger / Redoc docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]


# """config URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# from .views import ProtectedView

# urlpatterns = [
#     path("protected/", ProtectedView.as_view(), name="protected"),
# ]
# urlpatterns += [
#     # path('admin/', admin.site.urls),

#     # JWT endpoints
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

# schema_view = get_schema_view(
#     openapi.Info(
#         title="University Management API",
#         default_version='v1',
#         description="API documentation for all modules",
#         contact=openapi.Contact(email="admin@example.com"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to UMS!")

# urlpatterns += [
#     path('admin/', admin.site.urls),
#     path('', home),
#      path('api-auth/', include('rest_framework.urls')),
#     path('api/accounts/', include('accounts.urls')),
#     path('api/students/', include('students.urls')),
#     path('api/faculty/', include('faculty.urls')),
#     path('api/academics/', include('academics.urls')),
#     path('api/analytics/', include('analytics.urls')),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
# ]
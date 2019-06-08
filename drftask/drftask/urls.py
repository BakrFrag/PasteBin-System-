"""drftask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.documentation import include_docs_urls;
from django.contrib import admin
from django.urls import path,include
from django.conf import settings;
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Bins API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("rest/",include(('rest_framework.urls'),namespace='rest'),name="rest"),
    path("apis/",include(('bins.urls'),namespace="bins-api"),name="bins-api"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify',TokenVerifyView.as_view(),name="token_verify"),
    path("bins/docs/",include_docs_urls(title="Bins Restful Api")),
    path('swagger-docs/', schema_view,name="swagger"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),];

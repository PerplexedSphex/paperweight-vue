"""turbotier2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from rest_framework.routers import DefaultRouter

from accounts.viewsets import UserViewSet, AccountHolderViewSet
from people.viewsets import PersonViewSet


rest_framework_router = DefaultRouter()

rest_framework_router.register(
    prefix='person',
    viewset=PersonViewSet,
    base_name='person',
)

rest_framework_router.register(
    prefix='user',
    viewset=UserViewSet,
    base_name='user',
)

rest_framework_router.register(
    prefix='accountholder',
    viewset=AccountHolderViewSet,
    base_name='accountholder',
)


urlpatterns = [
    # todo - replace this with actual homepage which will presumably be the single-page application
    path('', RedirectView.as_view(pattern_name='dev-home'), name='home'),

    path('api/', include(rest_framework_router.urls), name='api-root'),
]

if settings.TESTING:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('', include('accounts.urls')),
        path('dev/', TemplateView.as_view(template_name='dev/dev_base.html'), name='dev-home')
    ]

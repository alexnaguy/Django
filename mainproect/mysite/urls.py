"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from app_forms.views import FormManage

from app_forms.views import RegisterUser

from app_forms.views import LoginUser, AvitoParse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FormManage.auto, name="auto"),
    path('get/', FormManage.get_info, name="get"),
    path('home/', FormManage.home, name = "home"),
    path('contacts/', FormManage.contacts, name = "contacts"),
    path('register/', RegisterUser.as_view(), name = "register"),
    path('login/', LoginUser.as_view(), name = "login"),
    path('news/', FormManage.news, name = "news"),
    path('create/', FormManage.create_form, name = "create"),
    path('table/', AvitoParse.parse_table, name = "table"),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

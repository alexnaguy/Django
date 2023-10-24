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
from django.contrib import admin
from django.urls import path
from app_forms.views import FormManage

from app_forms.views import RegisterUser

from app_forms.views import LoginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', FormManage.auto, name="auto"),
    path('get/', FormManage.get_info, name="get"),
    path('home/', FormManage.home, name = "home"),
    path('contacts/', FormManage.contacts, name = "contacts"),
    path('register/', RegisterUser.as_view(), name = "register"),
    path('login/', LoginUser.as_view(), name = "login"),



]

"""
URL configuration for djangoproect project.

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
from django.urls import path, re_path, include
from app1.views import Page, Page_two, NewCity 



history_patterns = [
    path('', NewCity.history, kwargs={"page": ""}, name="history"),
    path('people/', NewCity.history, kwargs={"page": "people"}, name="people"),
    path('photos/', NewCity.history, kwargs={"page": "photos"}, name="photos"),

]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hy/', Page.view_hello ),
    path('day/',Page.view_day_week),
    path('quot/', Page.random_title),
    path('time/', Page_two.show_time),
    path('table/', Page_two.multi_table),
    path('main/', NewCity.main, name= "main"),
    path('news/', NewCity.news, name= "news"),
    path('managers/', NewCity.managers_city, name = "managers" ),
    path('facts/', NewCity.facts_city, name = "facts" ),
    path('contacts/', NewCity.contacts, name = "contacts" ),
    path('history/', include(history_patterns)),
    #re_path(r'\w+', NewCity.main),  
]


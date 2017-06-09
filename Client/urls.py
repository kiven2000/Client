"""Client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from food.views import search, get_dish_detail, search_material
from customer.views import top_search_dish,recommend_dish

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', search),
    url(r'^top_search_dish/$', top_search_dish),
    url(r'^recommend_dish/$', recommend_dish),
    url(r'^get_dish_detail/', get_dish_detail),
    url(r'^search_material/', search_material)
]

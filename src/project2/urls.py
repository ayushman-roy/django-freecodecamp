"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages.views import home_view, contact_view, about_view

urlpatterns = [
    path('', home_view, name='home' ),
    path('contact/', contact_view, name='contact' ),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('article/', include('blog.urls')),
    path('journal/', include('journal.urls'))
]

# home, contact and about views are directly listed in this project url.py file
# url routes from products.urls file is indirectly listed here with the include function
# all urls listed in products.urls are children of the 'product/' url in the project
# this indirect route is used to include urls from different apps without cluterring the main url file
# it also allows code reusablity and improves code maintanence

"""
URL configuration for SCM project.

"""
from django.contrib import admin
from django.urls import path
from webapp.views import page


urlpatterns = [
    path('admin/', admin.site.urls),
	path('web/', page),
]




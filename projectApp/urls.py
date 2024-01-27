from django.contrib import admin # noqa
from django.urls import path # noqa
from projectApp.views import main


urlpatterns = [
    path('', main, name="main"),
]


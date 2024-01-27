
from django.contrib import admin # noqa
from django.urls import path,include # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectApp.urls')),
]

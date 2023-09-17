from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.simple_view),
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
]
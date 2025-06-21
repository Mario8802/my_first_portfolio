from django.contrib import admin
from django.urls import path, include

from certificates.views import certificate_list
from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path("certificates/", certificate_list, name="certificates"),
]

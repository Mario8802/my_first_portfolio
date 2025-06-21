# portfolio/urls.py   – опростена версия без github:
from django.contrib import admin
from django.urls import path, include

from portfolio import views  # home
from certificates.views import certificate_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

    # подсайтове
    path("projects/", include("projects.urls")),
    path("contact/", include("contact.urls")),
    path("certificates/", certificate_list, name="certificates"),
    path("github/", include("github.urls")),
    path("privacy/", views.PrivacyView.as_view(), name="privacy"),

]

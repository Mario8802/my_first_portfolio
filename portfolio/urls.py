from django.contrib import admin
from django.urls import path, include
from portfolio import views
from certificates.views import certificate_list
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("projects/", include("projects.urls")),
    path("contact/", include("contact.urls")),
    path("certificates/", certificate_list, name="certificates"),
    path("github/", include("github.urls")),
    path("privacy/", views.PrivacyView.as_view(), name="privacy"),
)

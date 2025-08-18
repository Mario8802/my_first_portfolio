from django.contrib import admin
from django.urls import path, include
from portfolio import views
from certificates.views import certificate_list
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.http import Http404

def fake_admin_404(request, *args, **kwargs):
    raise Http404()

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path(settings.ADMIN_URL, admin.site.urls),
    path("admin/", fake_admin_404, name="fake-admin"),
    path("", views.home, name="home"),
    path("projects/", include("projects.urls")),
    path("contact/", include("contact.urls")),
    path("certificates/", certificate_list, name="certificates"),
    path("github/", include("github.urls")),
    path("privacy/", views.PrivacyView.as_view(), name="privacy"),
)

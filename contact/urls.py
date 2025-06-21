from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),                      # /contact/
    path('submit/', views.contact_submit, name='contact_submit'),     # /contact/submit/
]

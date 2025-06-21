from django.shortcuts import render
from django.views.generic import TemplateView

class PrivacyView(TemplateView):
    template_name = "privacy.html"
def home(request):
    return render(request, "index.html")

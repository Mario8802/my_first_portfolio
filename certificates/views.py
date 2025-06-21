from django.shortcuts import render
from .models import Certificate


def certificate_list(request):
    certs = Certificate.objects.all()
    return render(request, "certificates.html", {"certs": certs})

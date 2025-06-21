from django.shortcuts import render

def github_view(request):
    return render(request, 'github/github.html')

from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')

def search(request):
    link = request.GET["context"]
    return render(request, 'search.html', {link : "link"})

def outcome(request):
    return render(request, 'outcome.html')

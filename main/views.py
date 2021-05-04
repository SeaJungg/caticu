from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')

def search(request):
    return redirect(outcome)

def outcome(request):
    return render(request, 'outcome.html')

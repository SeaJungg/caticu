from django.shortcuts import redirect, render

from .models import new


def index(request):
    return render(request, 'index.html')

def search(request):
    link = request.GET["context"]
    funding = new.objects.get(url = link)
    title = funding.title
    pnrate = funding.pnrate
    comment = funding.comment
    day0 = funding.day0
    day1 = funding.day1
    day2 = funding.day2
    day3 = funding.day3
    day4 = funding.day4
    day5 = funding.day5
    predict = funding.predict
    contents = {
        'title':title,
        'pnrate':pnrate,
        'comment':comment,
        'day0':day0,
        'day1':day1,
        'day2':day2,
        'day3':day3,
        'day4':day4,
        'day5':day5,
        'predict':predict,
        'origin_url':link
    }
    return render(request, 'search.html', contents)

def outcome(request):
    return render(request, 'outcome.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render (request, 'base.html')


def new_search (request):
    html = "<html><body>Amar BAL</body></html>"
    return HttpResponse (html)
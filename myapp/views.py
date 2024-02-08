from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def home(request):
    with open("myapp/stock_market_data.json") as f:
        data = json.load(f)
    return render(request, "home.html", {"data": data})


def test(request):
    with open("myapp/stock_market_data.json") as f:
        data = json.load(f)
    return render(request, "home.html", {"data": data})

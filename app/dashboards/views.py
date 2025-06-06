from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboards/index.html')

import os
from django.http import HttpResponse
from .utils import get_weather, send_to_slack


def weather(request):
    city = request.GET.get('city', 'Hanoi')
    message = get_weather(city)
    send_to_slack(message)
    return HttpResponse(message)

from django.shortcuts import render
from django.http import HttpResponse
from contextvars import Context
from datetime import datetime
from price.models import Developer
# Create your views here.

def index(request):
    return render(request, 'price/index.html')

def map(request):
    return render(request, 'price/map.html')

def predict(request):
    return render(request, 'price/predict.html')

def contact(request):
    return render(request, 'price/contact.html')

def feedback(request):
    return render(request, 'price/feedback.html')

# 각자
def doin(request):
    return render(request, 'contact/doin.html')

def dona(request):
    return render(request, 'contact/dona.html')

def ryu(request):
    return render(request, 'contact/ryu.html')

def song(request):
    return render(request, 'contact/song.html')

def mimi(request):
    return render(request, 'contact/mimi.html')

# 한꺼번에
def engineer_detail(request):
    context = dict()
    today = datetime.today().date()
    developer = Developer.objects.all()
    context["today"] = today
    context["developer"] = developer
    return render(request, 'contact/contact_base.html', context=context)
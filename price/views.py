# from itertools import Predicate
from django.shortcuts import render
from django.http import HttpResponse
from contextvars import Context
from datetime import datetime
from price.models import Developer
from price.models import Predict

import joblib
import pandas as pd
import lightgbm
from lightgbm import LGBMClassifier
import pickle


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




# def predict(request):
#     context = {'a':"ㅎㅡㄱ흐ㄱ흐긓ㄱ흑흑흑"}
#     return render(request, 'price/predict.html', context)

def make_bus_dict(dong):
    '''버스 노선 사전에서 동(key)를 넣으면 노선수(value)를 리턴하는 함수'''
    # 버스 노선 파일 불러오기
    bus_line_data = pd.read_excel("bus_line_data.xlsx")

    # 각 컬럼별 값들 리스트로 만들기
    adr_dong = list(bus_line_data['adr_dong'])
    bus_num = list(bus_line_data['버스노선수'])

    # dict로 키-값 형태로 저장하기
    bus_dict = {}

    for i in range(0, len(adr_dong)):
        bus_dict[adr_dong[i]] = bus_num[i]

    return bus_dict[dong]

reloadModel = joblib.load('./models/final_model.pkl')

def result(request):
    print(request)
    if request.method == 'POST':
        dong = str(request.POST.get('dong'))
        temp['year'] = request.POST.get('year')
        temp['area'] = request.POST.get('area')
        
    
    context = {'dong':dong, 'year':temp['year'], 'area':temp['area']}

    data_f = pd.DataFrame([temp])
    scoreval = reloadModel.predict(data_f)
    context = {'scoreval':scoreval}
    return render(request, 'price/result.html', context)







import numpy as np
from django.shortcuts import render
from scripts.weather_api import getWeatherData
from scripts.pred_main import model_pred
from scripts.validation import valid_form

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def wform(request):
    if request.method == 'POST':
        
        #validate form

        # Call fn
        predicted_yield = model_pred(request.POST['amb'], request.POST['mod'], request.POST['time'], request.POST['irr'])

        # Prepare the response
        context = {
            'predicted_yield': round(predicted_yield, 2),
        }
        print(predicted_yield)

        return render(request, 'form1.html', context)
    else:
        return render(request, 'form1.html')


def dform(request):
    if request.method == 'POST':
        
        #validate form

        # Call API
        lat, long, add, amb, irr = getWeatherData(request.POST['loc'], request.POST['date'], request.POST['time'])
        if add == "err":
            context = {
                'error': lat,
            }
            return render(request, 'form2.html', context)
        mod=amb
        hr = (request.POST['time']).split(':')[0]
        print(add)
        # Call fn
        predicted_yield = model_pred(amb, mod, hr, irr)

        # Prepare the response
        context = {
            'predicted_yield': round(predicted_yield, 2),
            'lat': lat,
            'long': long,
            'add': add,
            'amb': amb,
            'irr': irr,
        }
        print(context)

        return render(request, 'form2.html', context)
    else:
        return render(request, 'form2.html')
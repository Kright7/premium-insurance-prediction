from django.shortcuts import render
from django.http import HttpResponse
import joblib
import os
from django.conf import settings

# Correct the path to the model


model = joblib.load('statics/random_forest_regressor.pkl')

def home(request):
    return render(request, 'index.html')

def prediction(request):
    if request.method == 'POST':
        try:
            age = int(request.POST.get('age', 0))
            sex = int(request.POST.get('sex', 0))
            bmi = float(request.POST.get('bmi', 0))
            children = int(request.POST.get('children', 0))
            smoke = int(request.POST.get('smoke', 0))
            region = int(request.POST.get('region', 0))
            
            print(age, sex, bmi, children, smoke, region)
            
            pred = model.predict([[age, sex, bmi, children, smoke, region]])[0]
            print(round(pred))
            
            output = {'output': pred}
            return render(request, 'prediction.html', output)
        except Exception as e:
            print(f"Error occurred: {e}")
            return render(request, 'prediction.html', {'error': 'An error occurred during prediction.'})
    else:
        return render(request, 'prediction.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

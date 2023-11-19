from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from test_project.settings import API_KEY_WEATHER
from .forms import PostForm
import requests as req

def is_ajax(request):
  return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}&lang=ru'

    if request.method == 'POST' and is_ajax(request):
        form = PostForm(request.POST)
        if form.is_valid():
           # print(f'FROM FORM: \n{form.cleaned_data}')
            # get parameters from form for api call and  # request to api
            city_param_fac = form.cleaned_data['location']
            api_response = req.get(url.format(city_param_fac, API_KEY_WEATHER)).json()

            print(f'FROM API:\n{api_response}')
            return JsonResponse({"api_response": api_response}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    else:    
        form = PostForm() 
    
    return render(request, 'mainapp\index.html', {'form': form})



# time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(ti)) time from dt in unix
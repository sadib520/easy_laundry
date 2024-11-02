from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import custom_user  #! imported the custom user creted in models.py
import datetime


# Create your views here.
def log_in_page(request):
    year = datetime.datetime.now().year  
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        msg = '''
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Fira Code; text-align: center; background-color: whitesmoke;">
            <div>
                <p style="font-size: 32px; font-weight: none;">Credentials not valid!</p>
                <p style="font-size: 24px;">Go back & Try again.</p>
            </div>
        </div>
            '''


        if user is not None:
            login(request, user)
            return redirect('dash_path')
        else:
            return HttpResponse(msg)

  
    return render(request, 'login.html', {'year': year})



def reg(request):
    return render(request, 'reg.html')




def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # if not email or name or number:
        #     return JsonResponse({'error': 'All fields are required'})

        if pass1 != pass2:
            return JsonResponse({'error': "password doesn't match"})
        elif custom_user.objects.filter(email=email).exists():
            return JsonResponse({'error': "Email already exists"})
        else:
            user = custom_user.objects.create_user(name=name, email=email, number=number, password=pass1)
            return redirect('greet_path')

    return render(request, 'reg.html', {})


def greet(request):
    return render(request, 'greet.html', {})



def logout(request):
    logout(request)
    return redirect('home_path')



from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact_model
import time

# Create your views here.
def homepage(request):
    return render(request, 'landing/home.html')

def cards(request):
    return render(request, 'landing/dev.html')

def join(request):
    return render(request, 'landing/joinus.html')

from django.http import HttpResponse
from django.shortcuts import redirect, render

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        msg = request.POST.get("message")

        contact_instance = contact_model(name=name, number=number, email=email, msg=msg)
        contact_instance.save()
        
        # Adding a meta tag to refresh the page and redirect after 3 seconds
        response = '''
        <html>
        <head>
            <meta http-equiv="refresh" content="3; url=/" />
        </head>
        <body>
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Fira Code; text-align: center; background-color: whitesmoke;">
                <div>
                    <p style="font-size: 32px; font-weight: none;">Thank you for your submission.</p>
                    <p style="font-size: 24px; color: #2f6c48;">We will reach out to you soon.</p>
                </div>
            </div>
        </body>
        </html>
        '''

        return HttpResponse(response)

    return render(request, 'landing/contact.html')




def check_postal_code(request):
    if request.method == 'POST':
        postal_code = request.POST.get('postal_code')
        dict = {
            "Uttara": '1230',
            "Tongi": '1710',
            "Khagan": '1360'
        }

        if not postal_code.isdigit() or len(postal_code) != 4:
             return HttpResponse('<h1 style="color: red;">Postal code should be a 4-digit number !!</h1>')       
        
        for i, j in dict.items():
            if j == postal_code:
                return HttpResponse(f'<h1 style="color: green;">Do you mean {i}? We are available.</h1>')

        return HttpResponse('<h1 style="color: red;">We are currently not available in this area.</h1>')

    return render(request, 'landing/home.html')

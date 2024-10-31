from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'landing/LMS.html')

def cards(request):
    return render(request, 'landing/dev.html')

def join(request):
    return render(request, 'landing/joinus.html')

def contact(request):
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

    return render(request, 'landing/LMS.html')

from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'landing/about.html')


def laundry(request):
    return render(request, 'services/laundry.html')

def iron(request):
    return render(request, 'services/iron.html')

def dry(request):
    return render(request, 'services/dry.html')

def reg(request):
    return render(request, 'reg.html')
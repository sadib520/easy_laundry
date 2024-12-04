from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from login.models import custom_user



# Create your views here.
@login_required
def dashboard(request):
    # user = request.user #*this is the currently logged in user. it is django's built in user model, but if you use a custom user model, it will be an instance of that custom model.
    email = request.user.email
    user_name = custom_user.objects.raw('select id, name from login_custom_user where email = %s', [email])   #!returns a queryset
    name = None
    for user in user_name:
        name = user.name
        break
    print(name)
    print(user.is_authenticated)
    return render(request, 'dash/dash.html', {'name': name})


def order(request):

    return render(request, 'dash/order.html')

def buyplan(request):
    return render(request, 'dash/pricing.html')


def quantity(request):
    if request.method == "POST":
        try:
            # Retrieve POST data
            wash_type1 = request.POST.get("wash_type1", "")
            quantity1 = int(request.POST.get("quantity1", 0))
            wash_type2 = request.POST.get("wash_type2", "")
            quantity2 = int(request.POST.get("quantity2", 0))

            # Define prices for each wash type
            prices = {
                "Shirt": 10,
                "Pant": 15,
                "Towel": 5,
                "Bedsheet": 20,
            }

            # Calculate the total price
            total_price = (
                prices.get(wash_type1, 0) * quantity1
                + prices.get(wash_type2, 0) * quantity2
            )

            # Render the result back in the template
            return render(
                request,
                "dash/quantity.html",
                {"total_price": total_price},
            )
        except Exception as e:
            # Handle errors and show the message in the template
            return render(
                request,
                "dash/quantity.html",
                {"total_price": 0, "error": "Error calculating price."},
            )
    else:
        # Render an empty form with total price set to 0
        return render(request, "dash/quantity.html", {"total_price": 0})



def payment(request):
    return render(request, 'dash/payment.html')


def profile(request):
    email = request.user.email
    user_name = custom_user.objects.raw('select id, name, number from login_custom_user where email = %s', [email])

    name = None
    for user in user_name:
        name = user.name
        number = user.number
        break
    return render(request, 'dash/profile.html', {'name': name, 'number': number, 'email': email})


def update_profile_info(request):
    if request.method == 'POST':
        #retrieve form info
        name = request.POST.get('name')
        number = request.POST.get('number')
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        res = {
            "msg": "Credentials changed successfully!"
        }

        email = request.user.email
        obj = get_object_or_404(custom_user, email=email)
        if name:
            obj.name = name
        if number:
            obj.number = number
        if oldpass and newpass:
            obj.password = make_password(newpass)
        obj.save()
        return JsonResponse(res)
    
    return render(request, 'dash/profile.html')
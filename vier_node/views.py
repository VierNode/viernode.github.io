from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from vier_node.models import pricing_table, membership, contact_us, newsletter, login_details


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        data = membership(name=name, email= email, number= number, message= message)
        data.save()

       
    return render(request, "index.html")

def pricing(request):
 
    if request.method == "POST":
        package_name = request.POST.get('package_name')
        package_amount = request.POST.get('package_amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')

        ins = pricing_table(package_name=package_name, package_amount= package_amount, name=name, email=email, number=number, password=password)
        ins.save()
        print("Data saved Successfully")

    return render (request, "pricing.html")

def thanks(request):
    
    return render(request, "thanks.html")
def about(request):
    return render (request, "about.html")
def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        con = contact_us(name=name, email= email, number= number, message= message)
        con.save()
    return render (request, "contact.html")

def news_letter(request):
    if request.method == 'POST':
       
        email = request.POST.get('email')
        print(email)
        dat = newsletter(email= email)
        dat.save()
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = login_details(username=username, password=password)
            user.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'loginPage.html')



def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')
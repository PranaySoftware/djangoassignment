from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .models import *

# Create your views here.
def register_user(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user:
                return JsonResponse({'error': f'User with {username} already exists!'})
        except User.DoesNotExist:
            User(username=username, password=password).save()
            return redirect('/login/')


def authenticate_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid Authentication details'})

def logoutUser(request):
    logout(request)
    return redirect("/login/")

def get_products(request):
    if request.user.is_anonymous:
        return redirect("/login/") 
    products = UserProducts.objects.filter(user=request.user).values()
    products = list(products)

    return JsonResponse({'message': products})
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'googleauth/home.html')

def login_view(request):
    return redirect('/accounts/google/login/')


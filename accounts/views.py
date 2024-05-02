from django.shortcuts import render, redirect
from .models import CustomUser
# Create your views here.


def sign_up_and_login(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(
                username=username,
                phone=phone,
                password=password
                )
        user.save()
    
    return redirect('chat:lobby')



from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Вы успешно авторизованы")
        else:
            return HttpResponse("Ошибка")


# def homepage(request):
    # return render(request, "home.html")
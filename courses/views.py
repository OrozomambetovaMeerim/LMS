from .models import Student
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from .models import Student_answer



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

def Student(request):
    return render(request, "student.html")

class Student_answerCreateView(CreateView):
    model = Student_answer
    fields = ('name', 'email', 'subject_title', 'answer')
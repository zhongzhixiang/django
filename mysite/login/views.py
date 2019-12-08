from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import User
from .forms import RegisterForm
from .util import gen_secret

def login(request):
    return render(request, "login/login.html")

def register(request):
    return render(request, "login/regist.html")

class UserController:
    def userLogin(request):
        if request.method == 'POST':
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            password = gen_secret(password)
            print(password)
            # user = User.objects.get(user_name=user_name)
            user1 = User.objects.filter(user_name=user_name).filter(password=password).last()
            # if user.password != password:
            #     return HttpResponse("密码错误")
            # return render(request, "login/userinfo.html", {'user': user})
            if user1:
                request.session["user_name"] = user_name

                return render(request,'login/userinfor')

            else:
                return HttpResponse("账号或密码错误")

    def userRegist(request):
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        # User.objects.create(user_name=user_name, password=password, age=age)
        password = gen_secret(password)
        User.objects.create(user_name=user_name, password=password, age=age)
        return render(request, "login/login.html")


def yanzhengma(request):
    register_form = RegisterForm()
    return render(request, "index.html", {'register_form': register_form})


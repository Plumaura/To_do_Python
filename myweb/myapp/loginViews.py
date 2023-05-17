""" Login Module
------------------------------
Login View
- Authentication Login area

@login required
- If user is not login, route to login page
"""

from django.shortcuts import render
from django.views import View
from .models import Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# return render(request, "main.html", returnValues)
# -----> main.html로 returnValues 값을 가지고 간다

# return HttpResponse("안녕하세요")
# -----> 해당 링크에서 안녕하세요를 띄운다

# return redirect("main")
# -----> urls에서 name이 main이라는 url에 연결한다


class LoginView(View): # 작업중
    def get(self, request):

        loginForm = AuthenticationForm(request.POST)

        return render(request, "login.html")

    def post(self, request):
        loginForm = AuthenticationForm(request.POST)

        sendVals = {
            "loginForm" : loginForm
        }
        return render(request, "maintest.html", sendVals)


# @login_required(데코레이터)가 붙어있는 view는 로그인이 안되어 있으면 무조건 login으로 이동
@login_required
def main(request):

    user_all = Users.objects.all()
    # if selUser == "":
    # selUser = ""

    sendVals = {
    "user_all" : user_all,
    # "selUser" : selUser,
    }

    return render(request, "maintest.html", sendVals)
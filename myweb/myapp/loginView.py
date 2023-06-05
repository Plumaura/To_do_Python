""" Login Module
------------------------------
Login View
- Authentication Login area

@login required
- If user is not login, route to login page
"""

from django.shortcuts import render, redirect
from django.views import View
from .models import Users, TestUser, TestList
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

# return render(request, "main.html", returnValues)
# -----> main.html로 returnValues 값을 가지고 간다

# return HttpResponse("안녕하세요")
# -----> 해당 링크에서 안녕하세요를 띄운다

# return redirect("main")
# -----> urls에서 name이 main이라는 url에 연결한다


class LoginView(View): # 작업중
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        loginId = request.POST["loginId"]
        loginPw = request.POST["loginPw"]

        try:
            loginUser = TestUser.objects.filter(userId = loginId, userPw = loginPw).first()
        except TestUser.DoesNotExist:
            pass

        print(loginUser)
            
        if loginUser is not None:
            request.session['sessionNum'] = loginUser.userNum
            print(request.session['sessionNum'])
            print("로그인 성공")

            return redirect("main")
        else:
            noneUser = "noneUser"
            sendData = {
                "noneUser" : noneUser,
            }
            return render(request, "login.html", sendData)

        
        # user = authenticate(request, userId = insertId, userPw = insertPw)
        # login(request, user)

class LogoutView(View):
    def get(self, request):
        del request.session['sessionNum']
        
        return redirect("login")

    def post(self, request):
        del request.session['sessionNum']

        return redirect("login")
    


# @login_required(데코레이터)가 붙어있는 view는 로그인이 안되어 있으면 무조건 login으로 이동

def main(request):

    sessionId = request.session.get("sessionNum")

    if sessionId is not None:
        usersData = Users.objects.all()
        sendData = {
            "usersData" : usersData,
        }

        return render(request, "main.html", sendData)
    else:
        loginMessage = "sendLogin"
        sendData = {
            "loginMessage" : loginMessage,
        }

        return render(request, "main.html", sendData)

    

    # return render(request, "maintest.html", sendVals)
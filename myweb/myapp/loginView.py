""" Login Module
------------------------------
Login View
- Authentication Login area

@login required
- If user is not login, route to login page
"""

from django.shortcuts import render, redirect
from django.views import View
from .models import TestUser, TestList
import json
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

# return render(request, "main.html", returnValues)
# -----> main.html로 returnValues 값을 가지고 간다

# return HttpResponse("안녕하세요")
# -----> 해당 링크에서 안녕하세요를 띄운다

# return redirect("main")
# -----> urls에서 name이 main이라는 url에 연결한다

# @login_required(데코레이터)가 붙어있는 view는 로그인이 안되어 있으면 무조건 login으로 이동
# user = authenticate(request, userId = insertId, userPw = insertPw)
# login(request, user)


class LoginView(View):
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
            request.session['sessionName'] = loginUser.userName
            print(request.session['sessionNum'])
            print("로그인 성공")

            return redirect("main")
        else:
            noneUser = "noneUser"
            sendData = {
                "noneUser" : noneUser,
            }
            return render(request, "login.html", sendData)

class LogoutView(View):
    def get(self, request):
        del request.session['sessionNum']
        request.session.clear()
        
        return redirect("login")

    def post(self, request):
        del request.session['sessionNum']
        request.session.clear()

        return redirect("login")

class toLayer(View):
    def get(self, request):
        sessionNum = request.session.get("sessionNum")
        try:
            listToTest = TestList.objects.filter(userNum = sessionNum, listCheck = 0)

        except TestUser.DoesNotExist:
            print("리스트가 없습니다")

        sendData = {
            "listTo" : listToTest,
        }
        
        return render(request, "toLayer.html", sendData)
    
class doLayer(View):
    def get(self, request):
        sessionNum = request.session.get("sessionNum")
        try:
            listDoTest = TestList.objects.filter(userNum = sessionNum, listCheck = 1)

        except TestUser.DoesNotExist:
            print("리스트가 없습니다")

        sendData = {
            "listDo" : listDoTest,
        }
        
        return render(request, "doLayer.html", sendData)

def main(request):
    sessionNum = request.session.get("sessionNum")
    sessionName= request.session.get("sessionName")
    if sessionNum is not None:

        try:
            listToTest = TestList.objects.filter(userNum = sessionNum, listCheck = 0)
            listDoTest = TestList.objects.filter(userNum = sessionNum, listCheck = 1)

        except TestUser.DoesNotExist:
            print("리스트가 없습니다")

        sendData = {
            "sessionNum" : sessionNum,
            "sessionName" : sessionName,
            "listTo" : listToTest,
            "listDo" : listDoTest,
        }
        
        return render(request, "mainVue.html", sendData)
    else:
        loginMessage = "sendLogin"
        sendData = {
            "loginMessage" : loginMessage,
        }

        return render(request, "mainVue.html", sendData)
    
def linkedLogin(request):
    return redirect("login")

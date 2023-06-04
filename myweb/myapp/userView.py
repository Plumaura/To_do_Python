""" CRUD information
------------------------------
* Based on Create, Read, Update, Delete Model.
------------------------------
Now status (DB에 맞게 수정 예정):
    - Create : Finish
    - Read : Finish
    - Update : Finish
    - Delete : Finish
"""

from django.shortcuts import render,redirect
from django.views import View
from .models import Users, TestUser, TestList

class CreateView(View):
    def get(self, request):
        return render(request, "userCreate.html")

    def post(self, request):
        regNum = request.POST["regNum"]
        regId = request.POST["regId"]
        regPw = request.POST["regPw"]
        regPwC = request.POST["regPwC"]
        regName = request.POST["regName"]

        sameNum = "notSame"
        sameId = "notSame"
        sameName = "notSame"

        print(regNum, regId, regPw, regPwC, regName) # 테스트용 나중에 지워

        try:
            checkNum = TestUser.objects.filter(userNum = regNum)
            checkId = TestUser.objects.filter(userId = regId)
            checkName = TestUser.objects.filter(userName = regName)
        except TestUser.DoesNotExist:
            pass

        print(checkNum, checkId, checkName) # 테스트용 나중에 지워

        if len(checkNum) != 0:
            print("sameNum 있음") # 테스트용 나중에 지워
            sameNum = "sameNum"

        if len(checkId) != 0:
            print("sameId 있음") # 테스트용 나중에 지워
            sameId = "sameId"

        if len(checkName) != 0:
            print("sameName 있음") # 테스트용 나중에 지워
            sameName = "sameName"

        sendData = {
            "sameNum" : sameNum, "sameId" : sameId, "sameName" : sameName,
            "preNum" : regNum, "preId" : regId, "prePw" : regPw, "prePwC" : regPwC, "preName" : regName,
        }

        if (len(checkNum) == 0) and (len(checkId) == 0) and (len(checkName) == 0):
            TestUser.objects.create(userNum = regNum, userId = regId, userPw = regPw, userName = regName)
            return redirect("login")
        else:
            return render(request, "userCreate.html", sendData)

class UpdateView(View):

    def get(self, request):
        return render(request, "userUpdate.html")
        

    def post(self, request):
        updatePw = request.POST["updatePw"]
        updatePwC = request.POST["updatePwC"]
        updateName = request.POST["updateName"]

        sameName = "notSame"

        try:
            checkName = TestUser.objects.filter(userName = updateName)
        except TestUser.DoesNotExist:
            pass
        # 작업중 if문
        TestUser.objects.filter(userName = updateName).update(
            userName = updateName
        )

        if len(checkName) != 0:
            print("sameName 있음") # 테스트용 나중에 지워
            sameName = "sameName"

        sendData = {
            "sameName" : sameName
        }

        return redirect("main")

class DeleteView(View):

    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        deleteNum = request.POST["updateNum"]
        delUser = Users.objects.get(userNum = deleteNum)
        delUser.delete()

        return redirect("login")
    


class ReadView(View):

    def get(self, request):
        # To-do List 조회하는 html과 연결

        return render(request, "main.html")

    def post(self, request):
        select_Id = request.POST["select_Id"]
        selUser = Users.objects.filter(userId = select_Id) # -----> 값을 여러개 가져올 때 좋음 (제목 및 내용 검색)

        # select_Id = request.POST["select_Id"]
        # selUser = Users.objects.get(userId = select_Id) -----> 값을 하나만 가져올 때 좋음

        sendVals = {
            "selUser" : selUser,
        }
        
        return render(request, "view.html", sendVals)
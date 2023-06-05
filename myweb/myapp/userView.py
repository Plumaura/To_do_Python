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
from .models import TestUser, TestList

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

        try:
            checkNum = TestUser.objects.filter(userNum = regNum)
            checkId = TestUser.objects.filter(userId = regId)
            checkName = TestUser.objects.filter(userName = regName)
        except TestUser.DoesNotExist:
            pass

        print(checkNum, checkId, checkName)

        if len(checkNum) != 0:
            sameNum = "sameNum"

        if len(checkId) != 0:
            sameId = "sameId"

        if len(checkName) != 0:
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

        sessionNum = request.session.get("sessionNum")
        sameName = "notSame"

        try:
            checkName = TestUser.objects.filter(userName = updateName)
        except TestUser.DoesNotExist:
            pass

        if len(checkName) != 0:
            sameName = "sameName"
            sendData = {
                "sameName" : sameName,
                "prePw" : updatePw, "prePwC" : updatePwC, "preName" : updateName,
            }

            return render(request, "userUpdate.html", sendData)
        else:
            if (updateName != "") and (updatePw != ""):
                TestUser.objects.filter(userNum = sessionNum).update(
                    userName = updateName,
                    userPw = updatePw
                )
                request.session['sessionName'] = updateName

                return redirect("main")
            elif(updateName != "") and (updatePw == ""):
                TestUser.objects.filter(userNum = sessionNum).update(
                    userName = updateName
                )
                request.session['sessionName'] = updateName

                return redirect("main")
            elif(updateName == "") and (updatePw != ""):
                TestUser.objects.filter(userNum = sessionNum).update(
                    userPw = updatePw
                )

                return redirect("main")
            elif(updateName == "") and (updatePw == ""):
                noneData = "noneData"

                sendData = {
                    "noneData" : noneData
                }

                return render(request, "userUpdate.html", sendData)

class DeleteView(View):

    def get(self, request):
        sessionNum = request.session.get("sessionNum")
        delUser = TestUser.objects.get(userNum = sessionNum)
        delUser.delete()
        request.session.clear()

        return redirect("login")

    def post(self, request):
        sessionNum = request.session.get("sessionNum")
        delUser = TestUser.objects.get(userNum = sessionNum)
        delUser.delete()
        request.session.clear()

        return redirect("login")
    


# class ReadView(View): 필요없을 듯?

#     def get(self, request):
#         # To-do List 조회하는 html과 연결

#         return render(request, "main.html")

#     def post(self, request):
#         select_Id = request.POST["select_Id"]
#         selUser = Users.objects.filter(userId = select_Id) # -----> 값을 여러개 가져올 때 좋음 (제목 및 내용 검색)

#         # select_Id = request.POST["select_Id"]
#         # selUser = Users.objects.get(userId = select_Id) -----> 값을 하나만 가져올 때 좋음

#         sendVals = {
#             "selUser" : selUser,
#         }
        
#         return render(request, "view.html", sendVals)
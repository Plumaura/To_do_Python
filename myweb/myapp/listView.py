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
        return redirect("main")

    def post(self, request):
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)
        createTitle = request.POST["createTitle"]
        createContent = request.POST["createContent"]
        createCheck = request.POST["createCheck"]

        TestList.objects.create(userNum = userNum, listTitle = createTitle, 
                                listContent = createContent, listCheck = createCheck)
        
        return redirect("main")

class UpdateView(View):

    def get(self, request):
        return redirect("main")

    def post(self, request):
        updateNum = request.POST["finishNum"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)
        updateTitle = request.POST["updateTitle"]
        updateContent = request.POST["updateContent"]

        try:
            finishList = TestList.objects.filter(listNum = updateNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if len(finishList) != 0:
            noneUpdate = "noneUpdate"
            sendData = {
                "noneUpdate" : noneUpdate
            }

            return render(request, "userUpdate.html")
        else:
            finishList.update(listCheck = 1)

            return redirect("main")

class DeleteView(View):

    def get(self, request):
        sessionNum = request.session.get("sessionNum")
        delUser = TestUser.objects.filter(userNum = sessionNum)
        delUser.delete()
        request.session.clear()

        return redirect("login")

    def post(self, request):
        sessionNum = request.session.get("sessionNum")
        delUser = TestUser.objects.get(userNum = sessionNum)
        delUser.delete()
        request.session.clear()

        return redirect("login")
    
class ChangeView(View):

    def get(self, request):
        return redirect("main")

    def post(self, request):
        changeNum = request.POST["changeNum"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            changeList = TestList.objects.filter(listNum = changeNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        print(changeList)

        if len(changeList) != 0:
            changeList.update(listCheck = 1)

            return redirect("main")
        else:
            return redirect("main")
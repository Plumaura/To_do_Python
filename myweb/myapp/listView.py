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
        updateNum = request.POST["updateNum"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)
        updateTitle = request.POST["updateTitle"]
        updateContent = request.POST["updateContent"]

        try:
            updateList = TestList.objects.filter(listNum = updateNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if len(updateList) != 0:
            updateList.update(listTitle = updateTitle, listContent = updateContent)

            return redirect("main")
        else:
            return redirect("main")

class DeleteView(View):

    def get(self, request):
        deleteNum = request.POST["deleteNum"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            deleteList = TestList.objects.filter(listNum = deleteNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if len(deleteList) != 0:
            deleteList.delete()

            return redirect("main")
        else:
            return redirect("main")

    def post(self, request):
        deleteNum = request.POST["deleteNum"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            deleteList = TestList.objects.filter(listNum = deleteNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if len(deleteList) != 0:
            deleteList.delete()

            return redirect("main")
        else:
            return redirect("main")
    
class ChangeView(View):

    def get(self, request):
        return redirect("main")

    def post(self, request):
        changeNum = request.POST["changeNum"]
        typeList = request.POST["typeList"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            changeList = TestList.objects.filter(listNum = changeNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if typeList == "valueTo":
            changeList.update(listCheck = 1)
            
            return redirect("main")
        elif typeList == "valueDo":
            changeList.update(listCheck = 0)

            return redirect("main")
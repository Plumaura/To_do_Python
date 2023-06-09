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
        return render(request, "createList.html")

    def post(self, request):
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)
        createTitle = request.POST["createTitle"]
        createContent = request.POST["createContent"]

        TestList.objects.create(userNum = userNum, listTitle = createTitle, 
                                listContent = createContent, listCheck = 0)
        
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

            return redirect("toLayer")
        else:
            return redirect("toLayer")

class DeleteView(View):

    def get(self, request):
        deleteNum = request.POST["deleteNum"]
        typeList = request.POST["typeList"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            deleteList = TestList.objects.filter(listNum = deleteNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if typeList == "valueTo":
            deleteList.delete()
            
            return redirect("toLayer")
        elif typeList == "valueDo":
            deleteList.delete()

            return redirect("doLayer")

    def post(self, request):
        deleteNum = request.POST["deleteNum"]
        typeList = request.POST["typeList"]
        sessionNum = request.session.get("sessionNum")
        userNum = TestUser.objects.get(userNum = sessionNum)

        try:
            deleteList = TestList.objects.filter(listNum = deleteNum, userNum = userNum)
        except TestList.DoesNotExist:
            pass

        if typeList == "valueTo":
            deleteList.delete()
            
            return redirect("toLayer")
        elif typeList == "valueDo":
            deleteList.delete()

            return redirect("doLayer")
    
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
            
            return redirect("toLayer")
        elif typeList == "valueDo":
            changeList.update(listCheck = 0)

            return redirect("doLayer")
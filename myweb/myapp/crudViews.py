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
from .models import Users

class CreateView(View):
    def get(self, request):
        # To-do List 작성하는 html과 연결

        return render(request, "main.html")

    def post(self, request):
        # if request.POST.get("form_type") == "insert_form":
        regName = request.POST["insert_Name"]
        regId = request.POST["insert_Id"]
        regPw = request.POST["insert_Pw"]
        Users.objects.create(userName = regName, userId = regId, userPw = regPw)

        return redirect("main")


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


class UpdateView(View):

    def get(self, request):
        # To-do List 수정하는 html과 연결

        return render(request, "main.html")
        

    def post(self, request):
        update_Id = request.POST.get("update_Id")
        Users.objects.filter(userId = update_Id).update(
            userName = request.POST.get("update_Name")
        )

        return redirect("main")


class DeleteView(View):

    def get(self, request):
        # To-do List 삭제하는 html과 연결 # 필요한가?

        return render(request, "main.html")

    def post(self, request):
        # if request.POST.get("form_type") == "delete_form":
        delete_Name = request.POST.get("delete_Name")
        delUser = Users.objects.get(userName = delete_Name)
        delUser.delete()

        return redirect("main")
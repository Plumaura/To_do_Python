from django.shortcuts import render,redirect
from django.views import View
from myapp.models import Users
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

        loginForm = AuthenticationForm()

        return render(request, "login.html")

    def post(self, request):
        loginForm = AuthenticationForm(request.POST)
        pass


# @login_required(데코레이터)가 붙어있는 view는 로그인이 안되어 있으면 무조건 login으로 이동
@login_required
def main(request):

    user_all = Users.objects.all()
    # if selUser == "":
    # selUser = ""

    returnValues = {
    "user_all" : user_all,
    # "selUser" : selUser,
    }

    return render(request, "maintest.html", returnValues)


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

        returnValues = {
            "selUser" : selUser,
        }
        
        return render(request, "view.html", returnValues)


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
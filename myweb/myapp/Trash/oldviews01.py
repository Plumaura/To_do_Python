# from django.shortcuts import render, redirect
# from .models import Users

# def todo_login(request):
#     # Users라는 테이블에서 모든 객체를 가져옴
#     user_all = Users.objects.all()
#     selUser = ""

#     # POST 형식으로 입력된 값이 들어오면 실행
#     if request.method == "POST":
#         # form_type을 통해 SELECT, INSERT, DELETE, UPDATE 실행

#         # SELECT
#         if request.POST.get("form_type") == "select_form":
#             select_Id = request.POST.get("select_Id")
#             selUser = Users.objects.get(userId = select_Id)

#         # INSERT
#         if request.POST.get("form_type") == "insert_form":
#             regName = request.POST.get("insert_Name")
#             regId = request.POST.get("insert_Id")
#             regPw = request.POST.get("insert_Pw")
#             # POST 형식으로 입력된 값을 변수로 하여 DB에 등록 (Column = 변수)
#             Users.objects.create(userName = regName, userId = regId, userPw = regPw)

#         # DELETE
#         if request.POST.get("form_type") == "delete_form":
#             delete_Name = request.POST.get("delete_Name")
#             delUser = Users.objects.get(userName = delete_Name)
#             delUser.delete()

#         # UPDATE
#         if request.POST.get("form_type") == "update_form":
            
#             update_Id = request.POST.get("update_Id")
#             Users.objects.filter(userId = update_Id).update(
#                 userName = request.POST.get("update_Name")
#             )

#     returnValues = {
#         "user_all" : user_all,
#         "selUser" : selUser,
#     }
    
#     return render(request, "main.html", returnValues)
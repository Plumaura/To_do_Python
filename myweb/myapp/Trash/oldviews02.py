# from typing import Any
# from django.shortcuts import render,redirect
# from django.views import View
# from .models import Users

# # Class name : CRUDModules
# # def modules => C, R, U, D

# # Create your views here.
    
# def main(request):
#     if request.method== "POST":
#         if request.POST.get("form_type") == "insert_form":
#             modules_Create(request)
    
# def modules_Create(request):
#     setName = request.get("insert_Name")
#     setId = request.get("insert_Id")
#     setPwd = request.get("insert_Pw")
            
#     Users.objects.create(userName = setName, userId = setId, userPw = setPwd)
            
#     reValue = {
#         "test" : "hello",
#         "name" : setName,
#         "id" : setId,
#         "pwd" : setPwd,
#     }
        
#     return render(request, "classtest.html", reValue)

    
# def modules_Read(self, request):


#     return

    
# def modules_Update(self, request):


#     return
    
    
# def modules_Delete(self, request):


#     return




# class CreateView(View):
#     def __init__(self):
#         self.user_all = Users.objects.all()
#         all = "안녕"

#         self.sendValue = {
#             "user_all" : self.user_all,
#             "all" : all,
#         }

#     def get(self, request):

#         return render(request, "main.html", self.sendValue)

#     def post(self, request):
#         if request.POST.get("form_type") == "insert_form":
#             regName = request.POST.get("insert_Name")
#             regId = request.POST.get("insert_Id")
#             regPw = request.POST.get("insert_Pw")
#             Users.objects.create(userName = regName, userId = regId, userPw = regPw)

#         return render(request, "main.html", self.sendValue)

# class ReadView(View):

#     def get(self, request):
#         pass

#     def post(self, request):
#         pass

# class UpdateView(View):

#     def get(self, request):
#         pass

#     def post(self, request):
#         pass

# class DeleteView(View):

#     def get(self, request):
#         pass

#     def post(self, request):
#         pass

# class ModulesView(View):

#     def get(self, request):
#         reValues = {
#             "test" : "hello",
#         }
#         return render(request, "classtest.html", reValues)

#     def create(self, request):


#         return

#         # reValues = {
#         #     "test" : "hello",
#         # }
        
#         # return render(request, "classtest.html", reValues)

    
#     def modules_Read(self, request):


#         return

    
#     def modules_Update(self, request):


#         return
    
    
#     def modules_Delete(self, request):


#         return
    


# # class CRUD_Modules():

# #     def create()

# #     def read()

# #     def update()

# #     def delete()


# # class Create():
# #     def get() # sign up page 접속
    
# #     def post() create DB column
        
# # class Read():
# #     def get() # show page 접속
    
# #     def post() # SELECT DB column
        
# # class Update():
# #     def get() # modify page 접속
    
# #     def post() # UPDATE DB column
        
# # class delete():
# #     def get() # delete page 접속
    
# #     def post() DELETE DB column
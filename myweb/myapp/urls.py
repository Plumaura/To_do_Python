from django.urls import path
from myapp import loginViews, crudViews

urlpatterns = [
    path("login/", loginViews.LoginView.as_view(), name="login"),
    path("main/", loginViews.main, name="main"),
    
    path("create/", crudViews.CreateView.as_view(), name="create"),
    path("read/", crudViews.ReadView.as_view(), name="read"),
    path("upload/", crudViews.UpdateView.as_view(), name="update"),
    path("delete/", crudViews.DeleteView.as_view(), name="delete"),
]
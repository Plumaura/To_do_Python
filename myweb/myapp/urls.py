from django.urls import path
from myapp import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("main/", views.main, name="main"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("read/", views.ReadView.as_view(), name="read"),
    path("upload/", views.UpdateView.as_view(), name="update"),
    path("delete/", views.DeleteView.as_view(), name="delete"),
]
from django.urls import path
from myapp import loginView, userView, listView

urlpatterns = [
    path("login/", loginView.LoginView.as_view(), name="login"),
    path("logout/", loginView.LogoutView.as_view(), name="logout"),
    
    path("vueLogin/", loginView.main, name='vue'),
    path("main/", loginView.main, name="main"),
    
    path("searchTest/", loginView.main, name="login"),

    path("user/create/", userView.CreateView.as_view(), name="user_create"),
    path("user/update/", userView.UpdateView.as_view(), name="user_update"),
    path("user/delete/", userView.DeleteView.as_view(), name="user_delete"),

    path("list/create/", listView.CreateView.as_view(), name="list_create"),
    path("list/update/", listView.UpdateView.as_view(), name="list_update"),
    path("list/delete/", listView.DeleteView.as_view(), name="list_delete"),
    
    # path("create/", userView.CreateView.as_view(), name="create"),
    # path("read/", userView.ReadView.as_view(), name="read"),
    # path("upload/", userView.UpdateView.as_view(), name="update"),
    # path("delete/", userView.DeleteView.as_view(), name="delete"),
]
from django.urls import include, path
from myapp import loginView, userView, listView

urlpatterns = [
    # path("login/", loginView.LoginView.as_view(), name="login"),
    path("", loginView.linkedLogin),
    path("login/", loginView.LoginView.as_view(), name="login"),
    path("logout/", loginView.LogoutView.as_view(), name="logout"),
    path("toLayout/", loginView.toLayer.as_view() , name='toLayer'),
    path("doLayout/", loginView.doLayer.as_view() , name='doLayer'),
    path("mainVue/", loginView.main, name='main'),
    # path("main/", loginView.main, name="main"),
    

    path("user/create/", userView.CreateView.as_view(), name="user_create"),
    path("user/pwUpdate/", userView.UpdateView.as_view(), name="pw_update"),
    path("user/nickUpdate/", userView.UpdateView.as_view(), name="nick_update"),
    path("user/delete/", userView.DeleteView.as_view(), name="user_delete"),

    path("list/create/", listView.CreateView.as_view(), name="list_create"),
    path("list/update/", listView.UpdateView.as_view(), name="list_update"),
    path("list/delete/", listView.DeleteView.as_view(), name="list_delete"),
    path("list/change/", listView.ChangeView.as_view(), name="list_change"),
    
    # path("create/", userView.CreateView.as_view(), name="create"),
    # path("read/", userView.ReadView.as_view(), name="read"),
    # path("upload/", userView.UpdateView.as_view(), name="update"),
    # path("delete/", userView.DeleteView.as_view(), name="delete"),
]
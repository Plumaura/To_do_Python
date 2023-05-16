from django.urls import path
from myapp import views, oldviews

urlpatterns = [
    # path("", oldviews.todo_login, name="login"), # oldviews.py와 연결
    path("", oldviews.todo_login, name="login"),
    path("create", views.main, name="login"),
    # path("create/", ModulesView.as_view(method=["get"])),
]
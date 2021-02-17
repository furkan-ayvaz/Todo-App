from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("add/",views.todoAdd,name = "add"),
    path("delete/<int:id>",views.todoDelete,name = "delete"),
    path("update/<int:id>",views.todoUpdate,name = "update"),
]
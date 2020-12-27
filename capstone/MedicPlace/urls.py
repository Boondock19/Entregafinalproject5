from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("register",views.register_view,name="register"),
    path("logout",views.logout_view,name="logout"),
    path("Data_Sheet/<int:id>",views.data_sheet,name="Data_Sheet"),
    path("Data_Sheet/Rate_Dr/<int:id>",views.Rate_Dr,name="Rate_Dr"),
    path("NewArticle",views.New_Article_view,name="New_Article"),
    path("Article/<int:id>",views.Article_view,name="Article"),
    path("Edit_Article/<int:id>",views.Edit_Article_view,name="Edit_Article"),
    path("Article_edit_comment/<int:id>",views.Edit_Article_comment_view,name="Edit_Article_comment"),
    path("Medicine_type/<int:id>",views.Medicine_type_view,name="Medicine_type"),
    path("Medicine/<int:id>",views.Medicine_view,name="Medicine"),
    path("New_Medicine",views.New_Medicine_view,name="New_Medicine"),
    path("Edit_Medicine/<int:id>",views.Edit_medicine_view,name="Edit_Medicine"),
]
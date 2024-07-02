
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.ClassView_UserRegister.as_view() , name = "register"),
    path('login/', views.ClassView_UserLogin.as_view() , name = "login"),
    path('logout/', LogoutView.as_view() , name = "logout"),
    # path('logout/', views.ClassView_UserLogout.as_view() , name = "logout"),
    path('creat_album/', views.ClassView_AlbumViews.as_view() , name = "album_page"),
    path('edit/<int:id>', views.ClassView_EditAlbumViews.as_view() , name = "edit_album"),
    path('delete/<int:id>', views.ClassView_Delete.as_view() , name = "delete_album"),


    # path('creat_album/', views.AlbumViews , name = "album_page"),
    # path('edit/<int:id>', views.EditAlbumViews , name = "edit_album"),
    # path('delete/<int:id>', views.Delete_Album , name = "delete_album"),
]

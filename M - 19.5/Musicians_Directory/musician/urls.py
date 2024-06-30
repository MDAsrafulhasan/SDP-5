
from django.urls import path,include
from . import views
urlpatterns = [
    path('creat_musician/', views.ClassView_MusicianCreate.as_view() , name = "musician_page"),
    path('edit_musician/<int:id>', views.ClassView_EditMusicianView.as_view() , name = "edit_musician"),



    # path('creat_musician/', views.MusicianView , name = "musician_page"),
    # path('edit_musician/<int:id>', views.EditMusicianView , name = "edit_musician"),
]

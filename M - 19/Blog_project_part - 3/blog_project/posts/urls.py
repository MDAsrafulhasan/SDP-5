from django.urls import path , include
from . import views

urlpatterns = [
    # path('add/', views.add_post , name = 'add_post'),
    path('add/', views.ClassViewAddPost.as_view() , name = 'add_post'),
    # path('edit/<int:id>/', views.edit_post , name = 'edit_post'),
    path('edit/<int:id>/', views.ClassViewEditPost.as_view() , name = 'edit_post'),
    # path('delete/<int:id>/', views.delete_post , name = 'delete_post'),
    path('delete/<int:id>/', views.ClassViewDeletePost.as_view() , name = 'delete_post'),
    
    path('detail/<int:id>/', views.ClassView_DetailsView.as_view() , name = 'detail_post'),
]

from django.urls import path
from . import views
urlpatterns = [

    # path('', views.car , name = 'carpage'),
    path('signup/', views.ClassView_Signup.as_view() , name = 'signup'),
    path('login/', views.ClassView_Login.as_view() , name = 'login'),
    path('logout/', views.ClassView_Logout.as_view() , name = 'logout'),
    # path('profile/', views.ClassView_Profile.as_view() , name = 'profile'),
    path('profile/', views.profile , name = 'profile'),
]

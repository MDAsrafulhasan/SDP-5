from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.userlogin, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.userlogout, name = 'logout'),
    path('change_pass/', views.change_pass, name = 'change_pass'),
    path('change_pass2/', views.change_pass2, name = 'change_pass2'),
]

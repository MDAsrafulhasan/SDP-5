from django.urls import path , include
from . import views

urlpatterns = [
    path('register/', views.register , name = 'register'),

    # path('login/', views.user_login , name = 'user_login'),
    path('login/', views.ClassView_UserLogin.as_view() , name = 'user_login'),

    path('profile/', views.profile , name = 'profile'),
    path('profile/edit', views.edit_profile , name = 'edit_profile'),

    # path('logout/', views.user_logout , name = 'user_logout'),
    path('logout/', views.LogoutView.as_view() , name = 'user_logout'),

    path('profile/edit/pass_change/', views.pass_change , name = 'pass_change'),
]

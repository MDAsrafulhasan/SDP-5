from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [

    # path('', views.car , name = 'carpage'),
    path('signup/', views.ClassView_Signup.as_view() , name = 'signup'),
    path('login/', views.ClassView_Login.as_view() , name = 'login'),
    # path('logout/', views.ClassView_Logout.as_view() , name = 'logout'),
    path('logout/', LogoutView.as_view() , name = 'logout'),
    path('profile/', views.ClassView_Profile.as_view() , name = 'profile'),
    path('profile/edit', views.ClassView_UpdateProfile.as_view() , name = 'edit_profile'),
    path('car_dtails/<int:id>/', views.ClassView_CarDetails.as_view() , name = 'car_details'),
    path('buy_car/<int:id>/', views.buy_car , name = 'buy_car'),
    # path('profile/', views.profile , name = 'profile'),
]

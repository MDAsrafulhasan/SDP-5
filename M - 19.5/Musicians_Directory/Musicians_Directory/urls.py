
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('', views.ClassView_Home.as_view() , name= 'home_page'), #using class based view
    path('table_form/',views.ClassView_Table.as_view(),name = 'table_page' ),


    path('admin/', admin.site.urls),
    # path('', views.home , name= 'home_page'),
    path('album/', include("album.urls")),
    path('musician/', include("musician.urls")),
    # path('table_form/',views.table,name = 'table_page' ),
]

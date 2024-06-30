from django.urls import path,include
from . import views
urlpatterns = [
    # path('',views.home), # use for cookie
    path('',views.set_session), # use for session
    # path('get/',views.get_cookie), # use for cookie
    path('get/',views.get_session), # use for session,
    # path('delete/',views.delete_cookie), # use for cookie
    path('delete/',views.delete_session), # use for session
]

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import Resisteruser,logout

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register',Resisteruser.as_view(),name="register"),
    path('logout',logout.as_view(),name="logout"),
]
 
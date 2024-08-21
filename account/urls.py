from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from account import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register_page'),
    path('login/', obtain_auth_token, name='login_page'),
    path('logout/', views.LogoutApiView.as_view(), name='logout_page'),
]

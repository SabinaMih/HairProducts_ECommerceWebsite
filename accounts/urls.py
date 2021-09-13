from django.urls import path
from . import views
from .views import signupView, signinView, signoutView

app_name='accounts'

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('contactUs/', views.contactUs, name='contactUs'),
]
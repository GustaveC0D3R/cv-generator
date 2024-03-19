from django.urls import path
from . import views 

handler403 = 'accounts.views.csrf_failure'

urlpatterns = [
    path('home/login/register/', views.register, name = "register"),
    path('home/login/', views.user_login, name = "login"),
    path('home/', views.homepage, name = "homepage"),
    path('home/login/resume/', views.resume, name = "resume"),
]

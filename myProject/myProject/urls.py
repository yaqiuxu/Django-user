"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views.home import home
from user.views.userRegister import registerUser, activate
from user.views.userLogin import userLogin
from user.views.userStatus import userStatus

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("home/", home),
    path("login/", userLogin),
    path("register/", registerUser),
    path("activate/<uidb64>/<token>", activate, name='activate'),
    path("userStatus/", userStatus),
]

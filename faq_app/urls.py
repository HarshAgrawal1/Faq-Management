from django.contrib import admin
from django.urls import path,include
from faq_app import urls
from faq_app import views

urlpatterns = [
    path('', views.home , name='faq'),
    path('admin_login/',views.admin_login,name='admin_login'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/',views.login,name='login'),
    path('dashboard/newfaq/',views.newfaq,name="newfaq"),
    path('dashboard/newfaq/newpost/',views.newpost,name='newpost'),
]
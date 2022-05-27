from django.urls import path,re_path
from . import views

urlpatterns=[
    path=path ('',views.home_page,name='newsToday'),
]
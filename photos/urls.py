from django.urls import re_path
from . import views


urlpatterns = [
    re_path ('^$',views.my_Photo,name='myPhoto'),
    re_path ('^today/$',views.news_of_day,name='newsToday'),
]
   
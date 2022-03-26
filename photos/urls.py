from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    re_path ('^$',views.my_Photo,name='myPhoto'),
    re_path ('^search/',views.search_results,name = 'search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

   
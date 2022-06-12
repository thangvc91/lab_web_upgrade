from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('reg', reg),
    path('search-user', search_user),
    path('getlistuser',get_list_user),
    path('searchclienturl',search_client_url),
    path('getclienturl',get_client_url),
    path('checkins',checkins),
    path('dt',datatable),
    path('doc2html',doc2html),
    path('checkstaff',checkstaff),
    path('searchstaff',search_staff_url),
    path('bat',bat),
    path('searchbat',search_bat),
    path('forgot',forgot)
]

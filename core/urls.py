from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 


urlpatterns = [
    path('', views.homepage),
    path('temple', views.temple_info),
    path('search/', views.searchpage),
    path('search_info', views.search_info),
    path('aboutus/', views.aboutpage),
    path('learn/', views.learnpage),
    path('register/', views.registerationpage , name = 'register'),
    path("profile/",views.profile, name='profile'),
    path('logout/', views.logout),
    path('nearbyme/',views.nearbypage),
    # path('get_temple_coordinates/', views.get_temple_coordinates, name='get_temple_coordinates'),
    path('submit_feedback',views.submit_feedback,name='submit_feedback'),
    path('index/',views.index),
    # path('api-auth/', include('rest_framework.urls'))
]
from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [

    path('',views.home, name='home'),
    path('log',views.log,name='log'),
    path('regis', views.regis, name="regis"),
    path('apply', views.apply, name='apply'),
    path('detail',views.detail,name='detail'),
    path('load-branches', views.load_branches, name='ajax_load_branches'),
    path('lout',views.lout,name='lout'),

]
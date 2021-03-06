from django.urls import path

from . import views

# set the backend url routes 
urlpatterns = [
    path('', views.home, name = 'home'),
    path ('new-search/', views.new_search, name = 'new_search'),
    
]
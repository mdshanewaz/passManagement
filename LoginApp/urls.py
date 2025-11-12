from django.urls import path
from LoginApp import views

app_name = 'LoginApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('search/', views.search_view, name='search'),
]

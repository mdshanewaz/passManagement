from django.urls import path
from PassApp import views

app_name = 'PassApp'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('edit/<int:id>/', views.credential_edit_view,name='edit'),
    path('add/', views.credential_add_view, name='add'),
    path('delete/<int:id>/', views.credential_delete_view, name='delete'),
    path('detail/<int:id>/', views.credential_detail_view, name='detail'),
]

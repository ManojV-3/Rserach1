from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-publication/', views.add_publication, name='add_publication'),
    path('edit-publication/<int:pk>/', views.edit_publication, name='edit_publication'),
    path('delete-publication/<int:pk>/', views.delete_publication, name='delete_publication'),
]

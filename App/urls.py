from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/update/<int:pk>/', views.note_update, name='note_update'),
    path('note/delete/<int:pk>/', views.note_delete, name='note_delete'),
    
    # Add these new URLs for recycle bin
    path('recycle-bin/', views.recycle_bin, name='recycle_bin'),
    path('note/restore/<int:pk>/', views.note_restore, name='note_restore'),
    path('note/permanent-delete/<int:pk>/', views.note_permanent_delete, name='note_permanent_delete'),
]
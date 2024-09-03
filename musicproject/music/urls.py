
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),  # This should map the root URL to the album_list view
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
]


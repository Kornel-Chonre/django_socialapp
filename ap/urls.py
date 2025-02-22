from django.urls import path
from .views import home, create_post, profile, edit_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('profile/', profile, name='profile'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]

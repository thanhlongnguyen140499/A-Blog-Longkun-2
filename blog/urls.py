from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create_blog_view, name='create_blog'),
    path('detail/<slug>/', views.detail_blog_view, name='detail_blog'),
    path('edit/<slug>/', views.edit_blog_view, name='edit_blog')
]
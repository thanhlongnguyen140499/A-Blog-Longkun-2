from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
    path('edit/', views.account_view, name='edit'),
    path('logout/', views.logout_view, name='logout'),
    path('must_authenticated/', views.must_authenticated_view, name='must_authenticated')
]
 
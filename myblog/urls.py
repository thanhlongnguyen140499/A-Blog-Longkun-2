from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', include('account.urls')),
    path('', include('personal.urls')),
    path('admin/', admin.site.urls),
]

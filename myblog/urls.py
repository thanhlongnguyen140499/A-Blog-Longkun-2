from django.contrib import admin
from django.urls import path, include
# from personal.views import (
#     home_screen_view,
# )

urlpatterns = [
    path('register/', include('account.urls')),
    path('', include('personal.urls')),
    path('admin/', admin.site.urls),
]

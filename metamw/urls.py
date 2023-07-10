from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', admin.site.urls),
    # Other URL patterns of your project
    path('api/', include('api.urls')),
]
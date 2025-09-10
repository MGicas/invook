from django.contrib import admin 
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inventory/', include('co.edu.uco.invook.urls.api.inventory.urls')),
    path('api/users/', include('co.edu.uco.invook.urls.api.users.urls')),
]

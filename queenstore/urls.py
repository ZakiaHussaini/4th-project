
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('items/', include('product.urls')),
    path('dashboard/', include('dashboard.urls')),
    
]

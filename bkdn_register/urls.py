from django.contrib import admin
from django.urls import path, include
from register import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('bkdn/', include(urls))
]

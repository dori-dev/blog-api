"""Project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

v1_urlpatterns = [
    path('post/', include('post.api.urls', namespace='post')),
    path('rest-auth/', include('dj_rest_auth.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:version>/', include(v1_urlpatterns)),
    path('api-auth/', include('rest_framework.urls')),
]

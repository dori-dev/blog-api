"""Project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

v1_urlpatterns = [
    path('post/', include('post.api.urls', namespace='post')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path(
        'rest-auth/registration/',
        include('dj_rest_auth.registration.urls'),
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urlpatterns)),
    path('api-auth/', include('rest_framework.urls')),
    path(
        'schema/',
        get_schema_view(title='Blog API'),
    )
]

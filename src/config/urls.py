"""Project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


TITLE = 'Blog API'
DESCRIPTION = 'Usage guide for blog api'

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
        get_schema_view(
            TITLE,
            DESCRIPTION,
        ),
    ),
    path(
        'docs/',
        include_docs_urls(
            TITLE,
            DESCRIPTION,
        ),
    ),
]

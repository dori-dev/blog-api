from rest_framework import permissions
from django.core.handlers.wsgi import WSGIRequest


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: WSGIRequest, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.author)
        print(request.user)
        return obj.author == request.user

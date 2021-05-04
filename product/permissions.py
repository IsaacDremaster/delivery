from rest_framework.permissions import BasePermission


class IsProductOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff


class IsCommentOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif request.method == 'DELETE':
            return obj.user == request.user or request.user.is_staff or request.user.is_superuser
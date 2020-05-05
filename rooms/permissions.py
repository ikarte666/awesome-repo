from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, room):
        return room.user == request.user

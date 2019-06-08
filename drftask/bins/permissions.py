from rest_framework import permissions;

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
class IsSharedWith(permissions.BasePermission):
    """
    Custom permission to only Allow Shared Users To Retrive Bin
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.shared_with == request.user
class IsPublicBin(permissions.BasePermission):
    """
    Custom permission to only Allow Bin For All If It Shared With Public
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.public

class IsPublic_IsSharedWith_IsOwner(
    permissions.BasePermission):
       """
       allow authenticated user to retrieve the bin if they created it or shared with them
       also allow anonymous user to retrieve bin if it shared with public
       """
      
       def has_object_permission(self, request, view, obj):
            
            return ((obj.public==True) or (obj.author==request.user) or (request.user in 
            obj.shared_with.all()));
        
                
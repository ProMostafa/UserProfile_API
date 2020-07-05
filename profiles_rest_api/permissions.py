from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow User to edit their own profile """

    def has_object_permission(self,request,view,obj):
        """ Check user if trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatusProfile(permissions.BasePermission):
        """ Allow User to edit their own status """

        def has_object_permission(self,request,view,obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            
            return obj.user_profile.id == request.user.id
            """
            if request.user.id % obj.user_profile.id == 0:
                return True
            else:
                return False
            """


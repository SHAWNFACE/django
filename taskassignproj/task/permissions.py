from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):    
        if request.user.is_authenticated():
            username = request.user.username
            m = models.UserProfile.objects.all()
            usr = None
            for m1 in m:
                if str(m1.user.username) == str(username):
                    usr = m1
                    break;
            return usr.user_type == "Admin"
        else:
            return False        



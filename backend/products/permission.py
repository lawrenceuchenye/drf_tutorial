from rest_framework import permissions

class IsStaffEditorPermssion(permissions.DjangoModelPermissions):
    
    def has_permission(self,request,view):
        perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }

        user=request.user
        if not user.is_staff:
            return False
        return super().has_permission(request,view)


class UserQuerySetMixin():
    user="user"
    allow_staff_view_all=False

    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset()
        user=self.request.user
        lookup_data={}
        lookup_data[self.user]=user
        if self.allow_staff_view_all and user.is_staff:
            return qs
        return qs.filter(**lookup_data)


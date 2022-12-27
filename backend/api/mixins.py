from .permissions import IsStaffEditorPermssion
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermssion]

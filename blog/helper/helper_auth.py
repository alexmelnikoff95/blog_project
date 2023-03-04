from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View


class IsStaffPerm(PermissionRequiredMixin, View):

    def has_permission(self):
        # user = self.request.user
        # return user.has_perm('polls.can_open') or user.has_perm('polls.can_edit')
        if self.request.user.is_staff:
            return True
        return False


class AuthView(PermissionRequiredMixin, View):

    def has_permission(self):
        if self.request.user.is_authenticated:
            return True
        return False

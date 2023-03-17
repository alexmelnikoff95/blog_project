from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.views import View


class IsStaffPerm(UserPassesTestMixin, View):

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class AuthView(UserPassesTestMixin, View):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        return False

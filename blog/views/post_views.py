from django.views import View

from blog.helper import AuthView


class PostDetailView(AuthView, View):
    pass

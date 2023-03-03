from blog.helper import AuthView
from blog.models import Post, Tag
from blog.views import BaseView


class IndexView(BaseView):
    template = 'index.html'

    def get(self, request):
        return self.render_response()


class PostListView(AuthView, BaseView):
    """Список постов"""

    template = 'post_list.html'

    def get(self, request):
        try:
            post = Post.objects.all()
        except ValueError:
            return 'ошибка получения данных'
        return self.render_response(context={'post': post})


class TagListView(AuthView, BaseView):
    """Список тегов"""

    template = 'tags_list.html'

    def get(self, request):
        try:
            tags = Tag.objects.all()
        except ValueError:
            return 'ошибка получения данных'
        return self.render_response(context={'tags': tags})
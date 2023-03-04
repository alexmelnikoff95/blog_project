from blog.forms import PostForm
from blog.helper import AuthView

from blog.mixin import DetailMixin, CreateMixin, DeleteMixin, UpdateMixin
from blog.models import Post


class PostDetailView(AuthView, DetailMixin):
    model = Post
    template = 'post_detail.html'


class PostCreateView(AuthView, CreateMixin):
    model_form = PostForm
    template = 'post_create.html'


class PostUpdateView(AuthView, UpdateMixin):
    model = Post
    model_form = PostForm
    template = 'post_update.html'


class PostDeleteView(AuthView, DeleteMixin):
    model = Post
    template = 'post_delete.html'
    redirect_url = 'index'

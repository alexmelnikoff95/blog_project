from blog.forms import TagForm
from blog.helper import AuthView
from blog.mixin import DeleteMixin, UpdateMixin, DetailMixin, CreateMixin
from blog.models import Tag


class TagDetailView(AuthView, DetailMixin):
    model = Tag
    template = 'tag_detail.html'


class TagCreateView(AuthView, CreateMixin):
    model_form = TagForm
    template = 'tag_create.html'


class TagUpdateView(AuthView, UpdateMixin):
    model = Tag
    model_form = TagForm
    template = 'tag_update.html'


class TagDeleteView(AuthView, DeleteMixin):
    model = Tag
    template = 'tag_delete.html'
    redirect_url = 'index'

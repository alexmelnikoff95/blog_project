from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from blog.helper import AuthView
from blog.models import Post, Tag


class BaseView(View):
    template = None

    def render_response(self, context=None):
        if not context:
            context = {}
        assert self.template, 'необходимо задать шаблон'
        return render(self.request, self.template, context=context)


class PostListView(BaseView):
    """Список постов"""

    template = 'home.html'

    def get(self, request):
        try:
            search_query = request.GET.get('search', '')

            if search_query:
                posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
            else:
                posts = Post.objects.all()

            paginator = Paginator(posts, 2)

            page_number = request.GET.get('page', 1)
            page = paginator.get_page(page_number)

            is_paginated = page.has_other_pages()

            if page.has_previous():
                prev_url = '?page={}'.format(page.previous_page_number())
            else:
                prev_url = ''

            if page.has_next():
                next_url = '?page={}'.format(page.next_page_number())
            else:
                next_url = ''

            context = {
                'posts': page,
                'is_paginated': is_paginated,
                'next_url': next_url,
                'prev_url': prev_url,

            }
        except ValueError:
            return 'ошибка получения данных'
        return self.render_response(context=context)


class TagListView(AuthView, BaseView):
    """Список тегов"""

    template = 'tag_list.html'

    def get(self, request):
        try:
            tags = Tag.objects.all()
        except ValueError:
            return 'ошибка получения данных'
        return self.render_response(context={'tags': tags})

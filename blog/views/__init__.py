from django.shortcuts import render
from django.views import View


class BaseView(View):
    template = None

    def render_response(self, context=None):
        if not context:
            context = {}
        assert self.template, 'необходимо задать шаблон'
        return render(self.request, self.template, context=context)

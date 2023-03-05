from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View


class DetailMixin(View):
    model = None
    template = None

    def get(self, request, slug):
        qs = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, context={
            self.model.__name__.lower(): qs,
            'admin_object': qs,
            'detail': True
        })


class CreateMixin(View):
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = self.model_form(request.POST)

        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        return render(request, self.model_form, context={'form': form})


class UpdateMixin(View):
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        try:
            qs = self.model.objects.get(slug__iexact=slug)
            if not qs.DoesNotExist():
                raise Http404
        except ValueError:
            return 'ошибка'

        form = self.model_form(instance=qs)

        return render(request, self.template, context={
            'form': form,
            self.model.__name__.lower(): qs
        })

    def post(self, request, slug):
        try:
            qs = self.model.objects.get(slug__iexact=slug)
            if not qs.DoesNotExist():
                raise Http404
        except ValueError:
            return 'ошибка'

        form = self.model_form(request.POST, instance=qs)

        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, self.template, context={
            'form': form,
            self.model.__name__.lower(): qs
        })


class DeleteMixin(View):
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        try:
            qs = self.model.objects.get(slug__iexact=slug)
            if not qs.DoesNotExist():
                raise Http404
        except ValueError:
            return 'ошибка'
        return render(request, self.template, context={self.model.__name__.lower(): qs})

    def post(self, request, slug):
        try:
            qs = self.model.objects.get(slug__iexact=slug)
            if not qs.DoesNotExist():
                raise Http404
            qs.delete()
        except ValueError:
            return 'ошибка'

        return redirect(reverse(self.redirect_url))

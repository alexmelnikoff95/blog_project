from blog.models import Tag
from core import celery_app as app


@app.task()
def test(b, c):
    a = b + c
    return a


@app.task()
def tag(title, slug):
    Tag.objects.create(title=title, slug=slug)

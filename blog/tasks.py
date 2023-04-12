from celery import Celery

from blog.models import Post
from core import celery_app as app


@app.task()
def test(b, c):
    a = b + c
    return a







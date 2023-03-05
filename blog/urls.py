from django.urls import path

from blog.views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, TagCreateView, TagListView, \
    PostListView, TagDetailView, TagUpdateView, TagDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_url'),
    path('post/create/', PostCreateView.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post_delete_url'),

    path('tag_list', TagListView.as_view(), name='tag_list_url'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdateView.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDeleteView.as_view(), name='tag_delete_url'),
]

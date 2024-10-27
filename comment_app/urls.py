from django.urls import path
from . import views

urlpatterns = [
path('query_comments/', views.query_comments, name='query_comments'),
    path('add_comment1/', views.add_comment1, name='add_comment1'),
    path('add_comment2/', views.add_comment2, name='add_comment2'),
    path('delete_comment1/<int:comment1_id>/', views.delete_comment1, name='delete_comment1'),
    path('delete_comment2/<int:comment2_id>/', views.delete_comment2, name='delete_comment2'),
    path('like/<str:comment_type>/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('unlike/<str:comment_type>/<int:comment_id>/', views.unlike_comment, name='unlike_comment'),
    path('get_all_comments/', views.get_all_comments, name='get_all_comments'),
    path('get_all_comment1/', views.get_all_comment1, name='get_all_comment1'),
    path('get_all_comment2/', views.get_all_comment2, name='get_all_comment2'),
    path('get_comment1_by_post_id/<int:post_id>/', views.get_comment1_by_post_id, name='get_comment1_by_post_id'),
    path('get_comment2_by_comment1_id/<int:comment1_id>/', views.get_comment2_by_comment1_id, name='get_comment2_by_comment1_id'),


]

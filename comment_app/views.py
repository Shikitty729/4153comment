from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Comment1, Comment2
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def query_comments(request):
    return render(request, 'comments.html')
@csrf_exempt
@require_http_methods(["POST"])
def add_comment1(request):
    data = json.loads(request.body)
    content = data.get('content')
    post_id = data.get('post_id')
    writter_uni = data.get('writter_uni')
    comment = Comment1.objects.create(post_id=post_id, content=content, writter_uni=writter_uni)
    return JsonResponse({'id': comment.id, 'message': 'Comment1 added successfully'})

@csrf_exempt
@require_http_methods(["POST"])
def add_comment2(request):
    data = json.loads(request.body)
    content = data.get('content')
    comment1_id = data.get('comment1_id')
    writter_uni = data.get('writter_uni')
    comment1 = get_object_or_404(Comment1, id=comment1_id)
    comment = Comment2.objects.create(comment1=comment1, content=content, writter_uni=writter_uni)
    return JsonResponse({'id': comment.id, 'message': 'Comment2 added successfully'})
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_comment1(request, comment1_id):
    comment = get_object_or_404(Comment1, id=comment1_id)
    comment.delete()
    return JsonResponse({'message': 'Comment1 deleted successfully'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_comment2(request, comment2_id):
    comment = get_object_or_404(Comment2, id=comment2_id)
    comment.delete()
    return JsonResponse({'message': 'Comment2 deleted successfully'})

@csrf_exempt
def like_comment(request, comment_type, comment_id):
    if comment_type == 'comment1':
        comment = get_object_or_404(Comment1, id=comment_id)
    else:
        comment = get_object_or_404(Comment2, id=comment_id)
    comment.likes += 1
    comment.save()
    return JsonResponse({'message': f'{comment_type} liked successfully', 'likes': comment.likes})

@csrf_exempt
def unlike_comment(request, comment_type, comment_id):
    if comment_type == 'comment1':
        comment = get_object_or_404(Comment1, id=comment_id)
    else:
        comment = get_object_or_404(Comment2, id=comment_id)
    if comment.likes > 0:
        comment.likes -= 1
    comment.save()
    return JsonResponse({'message': f'{comment_type} unliked successfully', 'likes': comment.likes})
@require_http_methods(["GET"])
def get_all_comments(request):
    comment1_list = list(Comment1.objects.all().values())
    comment2_list = list(Comment2.objects.all().values())
    return JsonResponse({'comment1': comment1_list, 'comment2': comment2_list})

@require_http_methods(["GET"])
def get_all_comment1(request):
    comments = list(Comment1.objects.all().values())
    return JsonResponse({'comment1': comments})

@require_http_methods(["GET"])
def get_all_comment2(request):
    comments = list(Comment2.objects.all().values())
    return JsonResponse({'comment2': comments})

@require_http_methods(["GET"])
def get_comment1_by_post_id(request, post_id):
    comments = list(Comment1.objects.filter(post_id=post_id).values())
    return JsonResponse({'comment1': comments})

@require_http_methods(["GET"])
def get_comment2_by_comment1_id(request, comment1_id):
    comments = list(Comment2.objects.filter(comment1_id=comment1_id).values())
    return JsonResponse({'comment2': comments})


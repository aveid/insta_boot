from django.shortcuts import render, get_object_or_404
from .models import Post


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post/posts.html", locals())


def detail_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "post/detail.html", locals())
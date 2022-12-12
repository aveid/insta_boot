from django.shortcuts import render, get_object_or_404, redirect

from author.models import Author
from .forms import PostForm
from .models import Post


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post/posts.html", locals())


def detail_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "post/detail.html", locals())


def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        author = get_object_or_404(Author, id=data.get("author"))
        Post.objects.create(title=data.get("title"),
                            description=data.get("description"),
                            author=author)
        return redirect("posts")
    return render(request, "post/create.html", locals())
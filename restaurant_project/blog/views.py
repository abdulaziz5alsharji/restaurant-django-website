from django.shortcuts import render
from . models import Post, Category, Comment
from taggit.models import Tag
from . forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    search_result = request.GET.get('q')
    if search_result:
        posts = posts.filter(
            Q(title__icontains=search_result)|
            Q(content__icontains=search_result)
        )
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", context={
        "posts": page_obj
    })



def post_details(request, idd: int):
    post = Post.objects.get(pk=idd)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse("blog:post_details", args=(idd, )))
        else:
            return render(request, "blog/post_details.html", context={
            "post": post,
            "categories": categories,
            "tags": tags,
            "comments": comments,
            "number_of_comments": Comment.objects.filter(post=post).count(),
            "form": form
        })
    return render(request, "blog/post_details.html", context={
        "post": post,
        "categories": categories,
        "tags": tags,
        "comments": comments,
        "number_of_comments": Comment.objects.filter(post=post).count(),
        "form": CommentForm()
    })


def post_by_tag(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    return render(request, "blog/post_list.html", context={
        "posts": posts
    })



def post_by_category(request, category):
    posts = Post.objects.filter(category__category_name=category)
    return render(request, "blog/post_list.html", context={
        "posts": posts
    })

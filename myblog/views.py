from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag
from comments.forms import CommentForm
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
import markdown
from django.core import serializers


# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'myblog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    post_detail.body = '''# 一级标题

## 二级标题

### 三级标题

- 列表项1
- 列表项2
- 列表项3

> 这是一段引用

​```
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
​``` '''
    post_detail.body = markdown.markdown(post_detail.body,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
    form = CommentForm()
    comment_list = post_detail.comment_set.all()
    context = {'postDetail': post_detail,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'myblog/detail.html', context)


def archives(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month).order_by('-created_time')
    return render(request, 'myblog/index.html', context={"post_list": post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'myblog/index.html', context={"post_list": post_list})


def createPost(request):
    cate = request.POST['category']
    print(cate)
    category = Category.objects.create(name=cate)
    post = Post()
    post.title = request.POST['title']
    post.excerpt = request.POST['excerpt']
    post.body = request.POST['body']
    post.author = User.objects.filter(pk=1)
    post.category = category
    post.save()

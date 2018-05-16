from django.shortcuts import render,get_object_or_404
from .models import Category,Post,Tag
from django.views.generic.list import ListView
from django.http import HttpResponse
import markdown2
# Create your views here.

def index (request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'myblog/index.html', context={'post_list': post_list})

def detail(request,pk):
    post_detail = get_object_or_404(Post,pk=pk)
    return render(request,'myblog/detail.html' ,context={"postDetail":post_detail})


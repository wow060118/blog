from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from django.urls import reverse
from .forms import CommentForm
from django.core import serializers
import json
from myblog.models import Post


# Create your views here.
def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = post

            comment.save()
            return redirect(reverse('blog:detail', kwargs={'pk': post.pk}))

        else:
            comment_list = post.comment_set.all()
            print(serializers.serialize('json',comment_list))
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'myblog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(reverse('blog:detail', kwargs={'pk': post.pk}))

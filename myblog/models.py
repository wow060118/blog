from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，我们使用了 TextField。
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 类目
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

from django.conf import settings
from django.db import models
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategory(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=128)
    list_display = ('name')
    search_fields = ['name']
    list_filter = ['name']

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=128)
    list_display = ('name')
    search_fields = ['name']
    list_filter = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    symbol = models.CharField(max_length=2)
    tags = models.ManyToManyField(BlogTag)
    byline = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog-img/')
    slug = models.SlugField(unique=True, max_length=128)
    content = RichTextUploadingField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    publish_on = models.DateField()
    list_display = ('title', 'category', 'tags', 'author',
                    'publish_on', 'created_on', 'updated_on')
    search_fields = ['title', 'byline', 'symbol']
    list_filter = ['publish_on', 'created_on']
    date_hierarchy = 'pub_date'

    def __str__(self):
        return self.slug


class BlogComment(models.Model):

    comment = models.TextField(
        max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    list_display = ('comment')
    search_fields = ['comment']
    list_filter = ['comment']

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment[:50], self.author.email)

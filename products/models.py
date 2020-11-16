from django.db import models
from accounts.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=128)
    image = models.ImageField(upload_to='category-img/')
    title = models.CharField(max_length=255)
    product_description = models.TextField(blank=True)
    description = models.CharField(max_length=255)
    meta = models.CharField(max_length=255)
    list_display = ('name')
    search_fields = ['name']
    list_filter = ['name']

    class Meta:
        verbose_name_plural = "Product Categories"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def summary_desc(self):
        if len(self.product_description) > 30:
            return self.product_description[:30]+'...'
        else:
            return self.product_description


class Product(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=128)
    website = models.URLField(max_length=250)
    youtube = models.URLField(max_length=250, blank=True)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='icon-img/')
    body = models.TextField()
    votes = models.ManyToManyField(User, related_name='votes', blank=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # if user delete models.CASACDE means delete product as well

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def total_vote(self):
        e = Product.objects.get(id=self.id)
        e.votes.all()  # Returns all Author objects for this Entry.
        e.votes.count()
        return e.votes.count()

    def total_vote_str(self):
        e = Product.objects.get(id=self.id)
        e.votes.all()  # Returns all Author objects for this Entry.
        e.votes.count()
        return str(e.votes.count())

    def summary_desc(self):
        if len(self.description) > 50:
            return self.description[:50]+'...'
        else:
            return self.description

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-img/')

    def __str__(self):
        return self.product.title + 'Image'


class ProductComment(models.Model):

    comment = models.TextField(
        max_length=1000, help_text="Enter comment about product here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    list_display = ('comment', 'comment_date')
    search_fields = ['comment', 'comment_date']
    list_filter = ['comment', 'comment_date']

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment[:50], self.author.email)

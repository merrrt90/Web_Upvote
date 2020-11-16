from django import template
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from products.models import Product, ProductCategory, ProductComment
from django.db.models import Q
register = template.Library()


@register.inclusion_tag('tags/navigation.html', takes_context=True)
def show_navigation(context):
    if context['request'].user.is_authenticated:
        user = context['request'].user
        products = Product.objects.filter(
            votes__id=user.id)\
            .extra(select={'creation_seq': 'products_product_votes.id'})\
            .order_by("-creation_seq")
        return {'products': products[:5], 'user': user, 'userlike_count': products.count}
    else:
        return


@register.inclusion_tag('tags/starred_products.html', takes_context=True)
def starred_products(context):
    if context['request'].user.is_authenticated:
        user = context['request'].user
        products = Product.objects.filter(
            votes__id=user.id)\
            .extra(select={'creation_seq': 'products_product_votes.id'})\
            .order_by("-creation_seq")
        return {'products': products, 'user': user, 'userlike_count': products.count}
    else:
        return


@register.inclusion_tag('tags/categorywidget.html')
def category_widget():
    categories = ProductCategory.objects.all()
    return {'categories': categories[:5]}


@register.inclusion_tag('tags/related_products.html')
def related_product_widget(product):
    products = Product.objects.filter(
        ~Q(id=product.id)).filter(Q(category=product.category))

    return {'products': products[:5]}


@register.inclusion_tag('tags/last_comments.html')
def last_comment_widget():
    comments = ProductComment.objects.all().filter(is_active=True).order_by('-id')
    return {'comments': comments[:5]}


def is_voted_tag(product, user):
    if user in product.votes.all():
        m = True
    else:
        m = False
    return m


register.filter(is_voted_tag)

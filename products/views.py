from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductCategory, Images, ProductComment
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.forms import modelformset_factory
from .forms import ProductCreateForm
from django.contrib import messages


def home(request):
    products = Product.objects.all().order_by('-created').filter(active=True)
    context = {'products': products}
    return render(request, 'products/home.html', context)


"""Product Operations"""


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    if product.active == False:
        return redirect('home')
    else:
        images = Images.objects.filter(product=product)
        comments = ProductComment.objects.filter(
            product=product, is_active=True).order_by('comment_date')
        context = {'product': product,
                   'images': images,
                   'comments': comments
                   }
        return render(request, 'products/detail.html', context)


@login_required(login_url="/accounts/signup")
@require_POST
def upvote(request, product_id):
    if not request.user.is_authenticated:
        pass

    else:
        if request.method == 'POST':
            product = get_object_or_404(Product, pk=product_id)
            if request.user in product.votes.all():
                product.votes.remove(request.user.id)
            else:
                product.votes.add(request.user.id)
        ctx = serializers.serialize('json', [product], ensure_ascii=False)
        return HttpResponse(ctx, content_type='application/json')


"""Product Operations End"""


"""Category Operations"""


def categories(request):
    categories = ProductCategory.objects.all().order_by('-id')
    context = {'categories': categories}
    return render(request, 'products/categories.html', context)


def category_detail(request, slug):
    category = ProductCategory.objects.get(slug=slug)
    products = Product.objects.filter(category=category).filter(active=True)
    context = {'products': products,
               'category': category
               }
    return render(request, 'products/category_detail.html', context)


"""Category Operations End"""


@login_required(login_url="/accounts/signup")
def create(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            product = Product()
            product = form.save(commit=False)
            product.owner = request.user
            product.save()

            for f in formset:
                try:
                    photo = Images(product=product,
                                   image=f.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break
            messages.success(request, "Product has been successfully created.")
            return redirect('home')
    else:
        form = ProductCreateForm()
        formset = ImageFormset(queryset=Images.objects.none())

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'products/create.html', context)


@login_required(login_url="/accounts/signup")
@require_POST
def add_comment(request):
    if not request.user.is_authenticated:
        pass

    else:
        if request.method == 'POST':
            print(request.POST['product_id'])
            product = get_object_or_404(
                Product, pk=request.POST['product_id'])
            comment = ProductComment()
            comment.author = request.user
            comment.comment = request.POST['comment']
            comment.is_active = False
            comment.comment_date = timezone.datetime.now()
            comment.product = product
            print(comment)
            comment.save()
            return redirect('/products/'+str(product.slug))

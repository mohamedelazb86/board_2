from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from .models import Post,Category,Review
from .forms import ReviewForm


def post_list(request):

    posts=Post.objects.all().prefetch_related('review_post').order_by('-id')

    category=Category.objects.all().prefetch_related('post_category').order_by('-id')[:5]

    title=request.GET.get('search_name')
    if title:
        posts=posts.filter(title__icontains=title)
    else:
        posts=posts
    
    category_id=request.GET.get('category_id')
    if category_id:
        posts=posts.filter(category_id=category_id)


    paginator = Paginator(posts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'posts':page_obj,
        'category':category
    }

    return render(request,'blog/post_list.html',context)



def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    title=request.GET.get('search_name')
    if title:
        search=Post.objects.filter(title_icontains=title)
    else:
        search=Post.objects.all()

    previous_post=Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post=Post.objects.filter(id__gt=post.id).order_by('id').first()

    reviews=Review.objects.filter(post=post)

    if request.method =='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=post
            myform.save()
            return redirect(f'/blog/{slug}')
    else:
        form=ReviewForm()

    category=Category.objects.all().prefetch_related('post_category')[:5]

   

    
    context={
        'post':post,
        'previous_post':previous_post,
        'next_post':next_post,
        'reviews':reviews,
        'form':form,
        'category':category,
        
        
    }
    return render(request,'blog/post_detail.html',context)
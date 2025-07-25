from datetime import date
from django.shortcuts import render,get_object_or_404
from  .models import Author,Posts

# Create your views here.

def starting_page(request):
    
    # sorted_posts = sorted(all_posts,key = get_date)
    latest_posts = Posts.objects.all().order_by('-date')[:3]
    return render(request , "blog/index.html",{
        "posts" : latest_posts
    })
    
def posts(request):
    all_posts = Posts.objects.all()
    return render(request , "blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request,slug ):
    all_posts = Posts.objects.all()
    identified_post = get_object_or_404(Posts,slug = slug)

    return render(request ,"blog/includes/post-detail.html",{
        "post":identified_post
    })

from django.shortcuts import render,HttpResponse,get_object_or_404,redirect, HttpResponseRedirect
from .models import Contact, Post, Comment
from django.db.models import F,Count
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gtts import gTTS
from django.core.files.storage import FileSystemStorage
import os


def home_view(request):
    if request.method =="POST": 
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            email = email,
            message = message,
        ) 

        return HttpResponse()
    posts = Post.objects.all()[:3]    
    context = {
        'posts':posts,
    }
    template = "home.html"
    return render(request, template, context)


def mp3(request,id):
    post = get_object_or_404(Post, id=id)
    folder='media/' 
    mytext = post.description
    mp3name = post.slug
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)   
    myobj.save(os.path.join('media', mp3name + ".mp3"))
    return HttpResponseRedirect(post.get_absolute_url())


def blog(request):
    if request.method =="POST": 
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        Contact.objects.create(
            email = email,
            message = message,
        ) 

        return HttpResponse('')
   
    posts = Post.objects.all().order_by('-published')
    query = request.GET.get('q')
    if query:
       posts = posts.filter(title__icontains=query)
    
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    if not page:
        page = paginator.num_pages
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context={
        'posts':posts,
    }   
    template = "blog.html" 
    return render(request, template, context)


def post_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    response_data = {}  
 

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        date = request.POST.get('date')

        response_data['name'] = name
        response_data['comment'] = comment
        response_data['date'] = date
      
        Comment.objects.create(
            name = name,
            email = email,
            comment = comment,
            post = post,
  
        )
        return JsonResponse(response_data)
    posts = Post.objects.all()
    query = request.GET.get('q')
    if query:
       posts = posts.filter(title__icontains=query)
    comments = Comment.objects.filter(post=post)
    commentss = Comment.objects.filter(post=post).annotate(book_count=Count('comment'))
    Post.objects.filter(id=post.id).update(views=F('views') + 1)
    context = {
        'post':post,
        'posts':posts,
        'comments':comments,
        'commentss':commentss,
    }
    template = "detail.html"
    return render(request, template, context)

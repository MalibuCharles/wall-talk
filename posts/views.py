import random
from multiprocessing import context
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print("next_url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = PostForm()
    return render(request, 'components/form.html', context={"form":form})

def post_list_view(request, *args, **kwargs):
    """
    REST API VIEW 
    Consume By JS
    return json data
    """
    qs = Post.objects.all()
    posts_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,150)} for x in qs]
    data = {
      "isUser": False,
      "response": posts_list
    }
    return JsonResponse(data)

def post_detail_view(request, post_id, *args, **kwargs):
    """
    REST API VIEW 
    Consume By JS
    return json data
    """
    data = {
     "id": post_id,
    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found" 
        status = 404     
    return JsonResponse(data, status=status)
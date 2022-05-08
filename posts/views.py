from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render


from .models import Post

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

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
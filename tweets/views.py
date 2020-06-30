from django.shortcuts import render
# own imports below
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    '''
    data = {
        "id": tweet_id,
        #"image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    
    return JsonResponse(data, status=status) 
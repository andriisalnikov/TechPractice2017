from django.shortcuts import render
from django.http import HttpResponse
# from .models import Post

import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

def index(request):
    return HttpResponse("Yahoo! It works :D")

# def post_list(request):
#     posts = Post.objects.order_by('published_date')
#     return render(request, 'html/index.html', {posts})
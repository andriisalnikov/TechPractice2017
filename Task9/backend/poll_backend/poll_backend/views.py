from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from poll_backend.models import Category
import json


@csrf_exempt
def get_categories(request):
    all_categories = Category.Category.objects.to_json()
    return HttpResponse("[{id:1, name:'Category1'},{id:2,name:'Category2'}]", content_type="application/json")


@csrf_exempt
def create_category(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_category = Category.Category(name=body["name"])
    new_category.save()
    return HttpResponse(json.dumps(body), content_type="application/json")

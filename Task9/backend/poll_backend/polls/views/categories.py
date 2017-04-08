from django.core.serializers import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from polls.models import Category, Competition


@csrf_exempt
def get_categories(request):
    competitionId = int(request.GET.get('competitionId', -1))
    competition = Competition.objects.get(pk=competitionId)
    categories = Category.objects.all().filter(competition=competition)
    results = [ob.as_json() for ob in categories]
    return HttpResponse(json.dumps(results), content_type="application/json")


@csrf_exempt
def create_category(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_category = Category(name=body["name"])
    new_category.competition = Competition.objects.get(pk=body["competitionId"])
    new_category.save()
    return HttpResponse(json.dumps(new_category.as_json()), content_type="application/json")

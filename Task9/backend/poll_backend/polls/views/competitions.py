from django.contrib.sessions import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from polls.models import User, Competition


@csrf_exempt
def get_competitions(request):
    all_categories = Competition.objects.all()
    return HttpResponse(serializers.serialize("json", all_categories), content_type="application/json")


@csrf_exempt
def create_competition(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_competition = Competition(name=body["name"])
    new_competition.creator = User.objects.get(pk=1)
    new_competition.save()
    return HttpResponse(json.dumps(body), content_type="application/json")

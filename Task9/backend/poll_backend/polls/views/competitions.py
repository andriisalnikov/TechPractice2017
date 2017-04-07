from django.contrib.sessions import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from polls.models import User, Competition


@csrf_exempt
def get_competitions(request):
    all_competitions = Competition.objects.all()
    results = [ob.as_json() for ob in all_competitions]
    return HttpResponse(serializers.serialize("json", results), content_type="application/json")


@csrf_exempt
def create_competition(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_competition = Competition(name=body["name"])
    new_competition.creator = User.objects.get(pk=1)
    new_competition.save()
    return HttpResponse(json.dumps(new_competition.as_json()), content_type="application/json")

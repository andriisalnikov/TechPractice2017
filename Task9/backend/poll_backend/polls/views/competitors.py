from django.core.serializers import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from polls.models import Category, Competition, Competitor


@csrf_exempt
def get_competitors(request):
    competitionId = int(request.GET.get('competitionId', -1))
    competition = Competition.objects.get(pk=competitionId)
    competitors = Competitor.objects.all().filter(competition=competition)
    results = [ob.as_json() for ob in competitors]
    return HttpResponse(json.dumps(results), content_type="application/json")


@csrf_exempt
def create_competitor(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_competitor = Competitor(firstName=body["firstName"], lastName=body["lastName"],
                                course=body["course"], speciality=body["speciality"])

    new_competitor.competition = Competition.objects.get(pk=body["competitionId"])
    new_competitor.save()
    return HttpResponse(json.dumps(new_competitor.as_json()), content_type="application/json")

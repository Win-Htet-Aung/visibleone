from django.http.response import JsonResponse
from .models import Challenge
from .serializers import ChallengeSerializer


def get_challenges(request):
    data = {"challenges": []}
    for c in Challenge.objects.all():
        data["challenges"].append(ChallengeSerializer(c).data)
    return JsonResponse(data)

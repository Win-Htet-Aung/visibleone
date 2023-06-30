import csv
from django.http.response import JsonResponse


def get_challenges(request):
    data = {"challenges": []}
    with open("API Test - Sheet1.csv", "rt") as file:
        reader = csv.DictReader(file)
        for c in reader:
            data["challenges"].append(c)
    return JsonResponse(data)

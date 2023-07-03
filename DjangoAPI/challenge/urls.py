from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import get_challenges
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('api/challenges', get_challenges, name="challenges"),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

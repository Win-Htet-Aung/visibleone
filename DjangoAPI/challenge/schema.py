import graphene
import csv
from graphene_django import DjangoObjectType
from .models import Challenge


class ChallengeType(DjangoObjectType):
    class Meta:
        model = Challenge
        fields = ('ChallengeID', 'ChallengeName', 'ChallengeSucessRate')


class Query(graphene.ObjectType):
    challenges = graphene.List(ChallengeType)

    def resolve_challenges(root, info):
        return Challenge.objects.all()

schema = graphene.Schema(query=Query)

import graphene
import csv


class Query(graphene.ObjectType):
    challenges = graphene.List(of_type=graphene.JSONString)

    def resolve_challenges(root, info):
        challenges = []
        with open("API Test - Sheet1.csv", "rt") as file:
            reader = csv.DictReader(file)
            for c in reader:
                challenges.append(c)
        return challenges

schema = graphene.Schema(query=Query)

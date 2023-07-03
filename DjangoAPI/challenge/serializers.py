from rest_framework import serializers


class ChallengeSerializer(serializers.Serializer):
    ChallengeID = serializers.IntegerField()
    ChallengeName = serializers.CharField()
    ChallengeSucessRate = serializers.DecimalField(max_digits=5, decimal_places=2)

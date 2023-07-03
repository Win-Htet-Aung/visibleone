from django.db import models


class Challenge(models.Model):
    ChallengeID = models.IntegerField(primary_key=True)
    ChallengeName = models.CharField(max_length=200)
    ChallengeSucessRate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.ChallengeName

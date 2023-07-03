# Generated by Django 4.2.2 on 2023-07-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('ChallengeID', models.IntegerField(primary_key=True, serialize=False)),
                ('ChallengeName', models.CharField(max_length=200)),
                ('ChallengeSuccessRate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

from django.db import models

from app.models import Award, User


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    point = models.PositiveIntegerField()
    award = models.ForeignKey(Award, on_delete=models.CASCADE)


class ChallengeItem(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_to_display = models.DateTimeField()


class ChallengeTransaction(models.Model):
    challenge_item = models.ForeignKey(ChallengeItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models

from app.models import User


class Award(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class AwardTransaction(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

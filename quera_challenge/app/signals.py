from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from app.models import ChallengeItem, ChallengeTransaction, AwardTransaction

User = get_user_model()

@receiver(post_save, sender=ChallengeTransaction)
def create_award_transaction(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            challenge_item = instance.challenge_item
            challenge = challenge_item.challenge

            all_done = all(
                ChallengeTransaction.objects.filter(challenge_item=item).exists()
                for item in ChallengeItem.objects.filter(challenge=challenge)
            )

            if all_done:
                award = challenge.award
                AwardTransaction.objects.create(
                    award=award,
                    user=instance.user,
                    created_at=instance.created_at
                )

                instance.user.point_earned += challenge.point
                instance.user.save()

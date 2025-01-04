from django.utils import timezone
from django.db.models import Exists, OuterRef

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import ChallengeItem, ChallengeTransaction
from app.serializers import ChallengeItemSerializer, ChallengePostSerializer


class ChallengeListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChallengeItemSerializer

    def get_queryset(self):
        today = timezone.now()
        today_start = today.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today
        challenge_items = ChallengeItem.objects.filter(
            date_to_display__range=(today_start, today_end)
        ).annotate(
            is_done=Exists(
                ChallengeTransaction.objects.filter(
                    challenge_item=OuterRef("pk"), user=self.request.user
                )
            )
        )

        return challenge_items


class CreateChallengeTransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChallengePostSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        challenge_item_ids = serializer.validated_data["challenge_item_ids"]

        if not challenge_item_ids:
            return Response(
                {"error": "No challenge_item_ids provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user

        for item_id in challenge_item_ids:
            try:
                challenge_item = ChallengeItem.objects.get(id=item_id)
            except ChallengeItem.DoesNotExist:
                return Response(
                    {"error": f"ChallengeItem with id {item_id} does not exist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if ChallengeTransaction.objects.filter(
                challenge_item=challenge_item, user=user
            ).exists():
                return Response(
                    {
                        "error": f"Transaction already exists for ChallengeItem with id {item_id}."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            ChallengeTransaction.objects.create(
                challenge_item=challenge_item,
                user=user,
            )

        return Response(
            status=status.HTTP_201_CREATED,
        )

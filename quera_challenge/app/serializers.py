import jdatetime

from rest_framework import serializers

from app.models import ChallengeItem


class ChallengeItemSerializer(serializers.ModelSerializer):
    is_done = serializers.BooleanField(read_only=True)
    jalali_date_to_display = serializers.SerializerMethodField()

    class Meta:
        model = ChallengeItem
        fields = ["title", "description", "is_done", "jalali_date_to_display"]

    def get_jalali_date_to_display(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.date_to_display).strftime("%Y/%m/%d")


class ChallengePostSerializer(serializers.Serializer):
    challenge_item_ids = serializers.ListField(child=serializers.IntegerField())

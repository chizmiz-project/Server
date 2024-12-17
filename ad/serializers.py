from rest_framework import serializers

from ad.models import Advertisement


class AdvertisementSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id','author_id','title','main_picture','price','status']

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
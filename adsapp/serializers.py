from adsapp.models import AdsData
from rest_framework import serializers


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdsData
        fields = '__all__'
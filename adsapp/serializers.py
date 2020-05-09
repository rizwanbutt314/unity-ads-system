from adsapp.models import AdsData
from rest_framework import serializers


class AdsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image_link = serializers.SerializerMethodField()
    hit_link = serializers.SerializerMethodField()

    def get_image_url(self, instance):
        request = self.context.get('request')
        return request.build_absolute_uri(instance.photo.url)

    def get_image_link(self, instance):
        request = self.context.get('request')
        return request.build_absolute_uri(instance.photo.url)

    def get_hit_link(self, instance):
        request = self.context.get('request')
        url = '/{0}/record_hit'.format(instance.id)
        return request.build_absolute_uri(url)

    class Meta:
        model = AdsData
        fields = ('id', 'bundle_id', 'image_url', 'active', 'image_link', 'hit_link')

from collections import OrderedDict
from rest_framework import serializers
from .models import Images


class ImagesSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='photo_id')
    color = serializers.CharField(source='dominant_color')
    # url = serializers.CharField(source='image')

    def to_representation(self, instance):
        result = super(ImagesSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

    class Meta:
        model = Images
        fields = ['album_id', 'id', 'title', 'url', 'width', 'height', 'color']

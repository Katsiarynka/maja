from creators.models import Creator
from rest_framework import serializers


# Serializers define the API representation.
class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator
        fields = ['name', 'website', 'bio', 'twitter', 'instagram', 'youtube', 'tiktok', 'creator_nickname', 'image', 'volume', 'quantity_sold']
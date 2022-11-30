
from creators.serializers import CreatorShortSerializer
from nft.models import NFT
from rest_framework import serializers


class NFTSerializer(serializers.ModelSerializer):
    creator = CreatorShortSerializer()
    class Meta:
        model = NFT
        fields = ['name', 'description', 'image', 'creator']

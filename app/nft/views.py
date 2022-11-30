from rest_framework import viewsets
from nft.serializers import NFTSerializer

from nft.models import NFT


# NFT View
class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
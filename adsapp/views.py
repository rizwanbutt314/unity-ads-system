from rest_framework import mixins, generics, filters, status
from .serializers import AdsData, AdsSerializer


# Create your views here.
class APIDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsData.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
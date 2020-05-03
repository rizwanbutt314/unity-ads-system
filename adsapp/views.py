from rest_framework import mixins, generics, filters, status
from .serializers import AdsData, AdsSerializer


# Create your views here.
class AdsListingAPIIndex(mixins.ListModelMixin,
                         generics.GenericAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        queryset = AdsData.objects.select_related('category')
        category = self.request.GET.get('category')

        if category:
            return queryset.filter(category__name=category)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

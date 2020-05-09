from rest_framework import mixins, generics, filters, status
from rest_framework.response import Response
from .serializers import AdsData, AdsSerializer


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


class AdsListingAPIDetail(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        ad_id = self.kwargs.get('pk')
        try:
            existing_ad = AdsData.objects.get(id=ad_id)
            existing_ad.ads_hit_count = existing_ad.ads_hit_count + 1
            existing_ad.save()
            return Response({'success': True, 'error': ''},
                            status=status.HTTP_200_OK)
        except AdsData.DoesNotExist:
            return Response({'success': False, 'error': 'Unknown Ad'},
                            status=status.HTTP_404_NOT_FOUND)

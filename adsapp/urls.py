from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ads$', views.AdsListingAPIIndex.as_view(), name='ads_listing_api'),
    url(r'^(?P<pk>\d+)/record_hit?$', views.AdsListingAPIDetail.as_view(), name='api_detail'),
]

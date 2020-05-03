from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ads$', views.AdsListingAPIIndex.as_view(), name='ads_listing_api'),
]

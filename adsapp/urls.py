from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ad/(?P<pk>\d+)/?$', views.APIDetail.as_view(), name='api_detail'),
]

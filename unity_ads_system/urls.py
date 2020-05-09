from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.conf.urls.static import static

# Admin panel settings
admin.site.site_title = "Cross Promotion Ads System"
admin.site.site_header = "Cross Promotion Ads System"
admin.site.index_title = 'Administration'
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Token)

urlpatterns = [
    url(r'^ads-admin/', admin.site.urls),
    url(r'^', include('adsapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

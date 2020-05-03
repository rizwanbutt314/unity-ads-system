from django.contrib import admin
from adsapp.models import AdsData

# Register your models here.
class AdsDataAdmin(admin.ModelAdmin):
    list_display = ('id','studio_name', 'store_link', 'hits', 'ad_status', 'uploaded_on')

admin.site.register(AdsData, AdsDataAdmin)

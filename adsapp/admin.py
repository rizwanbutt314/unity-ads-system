from django.contrib import admin
from adsapp.models import AdsData

# # Register your models here.
class AdsDataAdmin(admin.ModelAdmin):
    list_display = ('id','bundle_id', 'hit_link', 'ready', 'active', 'uploaded_on')

admin.site.register(AdsData, AdsDataAdmin)

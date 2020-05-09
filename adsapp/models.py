import os
from unity_ads_system.settings import MEDIA_ROOT, MEDIA_URL
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=MEDIA_ROOT, base_url=MEDIA_URL)


class AdCategory(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Name of Category")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class AdsData(models.Model):
    bundle_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Bundle ID")
    active = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos', storage=fs)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    ads_hit_count = models.IntegerField(
        default=0,
        help_text="Ads hit count")
    category = models.ForeignKey(
        'adsapp.AdCategory',
        null=True,
        on_delete=models.CASCADE,
        help_text="Category of the ad")

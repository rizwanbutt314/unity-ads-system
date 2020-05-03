import os
from unity_ads_system.settings import MEDIA_ROOT, MEDIA_URL
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=MEDIA_ROOT, base_url=MEDIA_URL)


class AdsData(models.Model):
    bundle_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Bundle ID")
    active = models.BooleanField(default=False)
    hit_link = models.TextField(
        max_length=255,
        help_text="Hit link")
    ready = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos', storage=fs)
    uploaded_on = models.DateTimeField(auto_now_add=True)

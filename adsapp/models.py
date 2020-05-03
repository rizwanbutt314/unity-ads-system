import os
from unity_ads_system.settings import MEDIA_ROOT, MEDIA_URL
from django.db import models
from django.core.files.storage import FileSystemStorage
from django_dropbox_storage.storage import DropboxStorage

# DROPBOX_STORAGE = DropboxStorage()

fs = FileSystemStorage(location=MEDIA_ROOT, base_url=MEDIA_URL)


class AdsData(models.Model):
    store_link = models.TextField(
        max_length=255,
        help_text="store link, e.g. playstore")
    hits = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="number of hits on app")
    studio_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Name of the studio")
    photo = models.ImageField(upload_to='photos', storage=fs)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    ad_status = models.BooleanField(default=False)

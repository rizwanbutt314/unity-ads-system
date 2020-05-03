from django.contrib import admin
from adsapp.models import AdsData, AdCategory


# # Register your models here.
class AdsDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'bundle_id', 'active', 'uploaded_on', 'category_name')

    def category_name(self, instance):
        if instance.category:
            return instance.category.name
        return ''


class AdCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on')


admin.site.register(AdsData, AdsDataAdmin)
admin.site.register(AdCategory, AdCategoryAdmin)

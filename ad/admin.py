from django.contrib import admin

from ad.models import Advertisement


# Register your models here.
@admin.register(Advertisement)
class AdvertiseAdmin(admin.ModelAdmin):
    pass
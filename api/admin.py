from django.contrib import admin
from api.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "size", "duration", "charge", "upload_date"]
    list_filter = ["charge"]


admin.site.register(Video, VideoAdmin)

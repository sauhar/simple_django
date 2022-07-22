import datetime
from django.db import models
import datetime


class Video(models.Model):
    title = models.CharField(max_length=60)
    upload_date = models.DateTimeField(default=datetime.datetime.now())
    video_file = models.FileField(null=True)
    duration = models.FloatField(null=True)
    size = models.FloatField(null=True)
    charge = models.FloatField(null=True)

    def __str__(self):
        return self.title

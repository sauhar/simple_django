import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Video
from moviepy.editor import VideoFileClip
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import string


# def convert_time(time):
#     if time<60:
#         return time "seconds"
#     elif time>60 and < 3600:


@csrf_exempt
@api_view(["POST", "GET"])
def upload(request):
    in_memory_file = request.FILES["file"]
    # print(get_video_length(thumbnail))
    # title = request.body.get("title")

    video = Video.objects.create()
    video.video_file = in_memory_file

    letters = string.ascii_lowercase
    number = "".join(random.choice(letters) for i in range(10))
    video.title = request.POST.get("title", "") + "_" + number

    video.save()
    clip = VideoFileClip(video.video_file.path)
    duration = clip.duration
    size = video.video_file.size
    print("duration", duration)
    print("size", video.video_file.size)

    if size > 1000000000 and duration > 600:
        return Response(
            "file size cannot be greater than 1 gb and file duration cannot be greater than 10 minutes"
        )

    elif video.video_file.size > 10000000000:
        video.delete()
        return Response("file size greater than 1 gb")

    elif duration > 600:
        video.delete()

        return Response("Video duration is greater than 10 minutes")

    else:
        charge = 0
        if size < 500000000:
            charge = 5
        else:
            charge = 12.5
        if duration < 378:
            charge = charge + 12.5
        else:
            charge = charge + 20
        video.duration = duration
        video.size = video.video_file.size
        video.charge = charge
        video.upload_date = datetime.datetime.now()
        video.save()
        return Response("your video has been saved")


@csrf_exempt
@api_view(["POST", "GET"])
def calculate_charge(request):
    in_memory_file = request.FILES["file"]
    # print(get_video_length(thumbnail))
    # title = request.body.get("title")

    print(request.data.get("title"))

    video = Video.objects.create()
    video.video_file = in_memory_file

    video.save()
    clip = VideoFileClip(video.video_file.path)
    duration = clip.duration
    size = video.video_file.size
    print("duration", duration)
    print("size", video.video_file.size)

    if size > 1000000000 and duration > 600:
        return Response(
            "file size cannot be greater than 1 gb and file duration cannot be greater than 10 minutes"
        )

    elif video.video_file.size > 10000000000:
        video.delete()
        return Response("file size greater than 1 gb")

    elif duration > 600:
        video.delete()

        return Response("Video duration is greater than 10 minutes")

    else:
        charge = 0
        if size < 500000000:
            charge = 5
        else:
            charge = 12.5
        if duration < 378:
            charge = charge + 12.5
        else:
            charge = charge + 20
        video.duration = duration
        video.size = video.video_file.size
        video.delete()
        return Response(f"your total charge is ${charge}")

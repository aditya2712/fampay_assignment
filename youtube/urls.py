from django.urls import path

from .views import VideosList

urlpatterns = [
    # GET /videos?tag=tag_name
    path("videos/", VideosList.as_view(), name="get_videos_list"),
]

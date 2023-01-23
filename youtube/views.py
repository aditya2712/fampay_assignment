from rest_framework import generics, serializers
from .models import Video
from rest_framework.pagination import PageNumberPagination


class VideosList(generics.ListAPIView):
    def get_queryset(self):
        tag = self.request.query_params.get("tag", None)
        if tag is not None:
            return Video.objects.filter(tag__name=tag).order_by("-published_date")
        return Video.objects.all().order_by("-published_date")

    class CustomPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = "page_size"
        max_page_size = 20
        page_query_param = "page"

    class VideoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Video
            fields = "__all__"

    serializer_class = VideoSerializer
    pagination_class = CustomPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.VideoSerializer(queryset, many=True)

        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

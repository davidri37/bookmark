from rest_framework import serializers
from .models import Bookmark
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .serializers import BookmarkSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.
class ApiBookmarkList(ListAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


class ApiBookmarkDetail(RetrieveUpdateDestroyAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


class ApiBookmarkCreate(CreateAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


class ApiBookmarkUpdate(UpdateAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


class ApiBookmarkDelete(DestroyAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer


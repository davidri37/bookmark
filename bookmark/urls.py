from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list')
]

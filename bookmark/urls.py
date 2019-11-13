from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiBookmarkList.as_view(), name='api'),
    path('api/<int:pk>/', ApiBookmarkCreate.as_view(), name='api_add'),
    path('api/<int:pk>/', ApiBookmarkDetail.as_view(), name='api_detail'),
    path('api/<int:pk>/', ApiBookmarkUpdate.as_view(), name='api_update'),
    path('api/<int:pk>/', ApiBookmarkDelete.as_view(), name='api_delete')
]

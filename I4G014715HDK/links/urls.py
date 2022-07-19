from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'api/links', LinkListApi, basename = 'api/links')

app_name="link"

urlpatterns = [
    path("", LinkListApi.as_view({'get':'list'}), name="api_list"),
    path("create/", LinkCreateApi.as_view({'get':'create'}), name="api_create"),
    path("update/<int:pk>", LinkUpdateApi.as_view({'get':'update'}), name="api_update"),
    path("delete/<int:pk>", LinkDeleteApi.as_view({'get':'delete'}), name="api_delete"),
    path("active/", ActiveLinkView.as_view(), name="active_link"),
    path("recent/", RecentLinkView.as_view(), name="recent_link"),
] 

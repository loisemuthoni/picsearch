from django.conf.urls import url
from .views import (
    # ImageListView,
    ImageDetailView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView,
    OtherProfile,
    ImageSearch,
    Index_View,
    CommentOnImage,
    Like,
)


urlpatterns = [
    url(r'^$',Index_View,name="index_view"),
    url(r'^image/(?P<pk>\d+)$',ImageDetailView.as_view(),name="image_detail"),
    url(r'^image/new$',ImageCreateView.as_view(),name="image_upload"),
    url(r'^image/(?P<pk>\d+)/update',ImageUpdateView.as_view(),name="image_update"),
    url(r'^image/(?P<pk>\d+)/delete',ImageDeleteView.as_view(),name="image_delete"),
    url(r'^user/(?P<pk>\d+)',OtherProfile,name="single_profile"),
    url(r'^search/$',ImageSearch,name="search-results"),
    url(r'^comment/(?P<pk>\d+)',CommentOnImage,name="image-comment"),
    url(r'^like/(?P<pk>\d+)',Like,name="image-like"),
]
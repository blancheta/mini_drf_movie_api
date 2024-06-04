from rest_framework import routers
from django.urls import path

from api.views import (
    UserViewSet, WatchListItemViewSet,
    MovieListAPIView, MovieRetrieveAPIView,
    MoviesByUserAPIView, RatingViewSet
)

router = routers.SimpleRouter()

router.register("users", UserViewSet)
router.register("watchlistitems", WatchListItemViewSet)
router.register("ratings", RatingViewSet)

urlpatterns = [
    path("users/<pk>/watchlist/", MoviesByUserAPIView.as_view()),
    path("movies/", MovieListAPIView.as_view(), name="list-movies"),
    path("movies/<pk>/", MovieRetrieveAPIView.as_view(), name="retrieve-movie"),
]

urlpatterns += router.urls

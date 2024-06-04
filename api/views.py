from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from api.models import Movie, WatchListItem, Rating
from api.serializers import MovieSerializer, WatchListItemSerializer, UserSerializer, UserWatchListSerializer, \
    RatingSerializer

User = get_user_model()


# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieListAPIView(ListAPIView):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveAPIView(RetrieveAPIView):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class WatchListItemViewSet(ModelViewSet):

    serializer_class = WatchListItemSerializer
    queryset = WatchListItem.objects.all()

    http_method_names = ["get", "post", "delete"]


class UserWatchListAPIView(RetrieveAPIView):

    model = User
    queryset = User.objects.all()
    serializer_class = UserWatchListSerializer

    fields = ["wishlist"]


class MoviesByUserAPIView(ListAPIView):

    serializer_class = MovieSerializer

    def get_queryset(self):
        # movie_ids = WatchListItem.objects.filter(
        #     user_id=self.kwargs["pk"]).values_list(
        #     "movie", flat=True
        # )
        # movies = Movie.objects.filter(id__in=movie_ids)

        user = User.objects.get(id=self.kwargs['pk'])
        movies = user.watchlist.all()

        return movies


class RatingViewSet(ModelViewSet):
    model = Rating
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
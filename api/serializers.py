from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, HyperlinkedModelSerializer
from django.contrib.auth import get_user_model

from api.models import Movie, WatchListItem, Genre, Rating

User = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ["slug", "name"]


class RatingSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Rating
        fields = ["slug"]


class UserWatchListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["watchlist"]


class MovieSerializer(ModelSerializer):

    genres = GenreSerializer(many=True)
    rating = HyperlinkedRelatedField(
        read_only=True,
        view_name='rating-detail'
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title", "synopsis", "released_date",
            "genres", "rating"
        ]


class WatchListItemSerializer(ModelSerializer):

    class Meta:
        model = WatchListItem
        fields = [
            "user",
            "movie",
            "watched"
        ]

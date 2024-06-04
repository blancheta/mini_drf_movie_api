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
            "user_id",
            "movie_id",
            "watched",
            "order"
        ]
        read_only_fields = ("order",)

    def validate(self, data):
        print("I am passing always here")
        return super().validate(data)

    def validate_user(self, value):
        print("Validating the user")
        return super().validate(value)

    def to_internal_value(self, data):

        new_data = data.copy()

        current_order_end = WatchListItem.objects.filter(user=data.get("user")).last()
        if current_order_end is not None:
            new_order = current_order_end + 1
        else:
            new_order = 1

        new_data["order"] = new_order

        return new_data

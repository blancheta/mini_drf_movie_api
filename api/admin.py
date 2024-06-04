from django.contrib import admin
from django.contrib.auth import get_user_model

from api.models import Genre, Rating, Movie, WatchListItem


User = get_user_model()

admin.site.register(User)
admin.site.register(Genre)


class RatingModelAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ["slug", "name", "description"]


admin.site.register(Rating, RatingModelAdmin)


class MovieModelAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ["title", "synopsis", "rating"]


admin.site.register(Movie, MovieModelAdmin)


class WatchListItemAdmin(admin.ModelAdmin):
    model = WatchListItem
    list_display = ["user", "movie", "order", "watched"]


admin.site.register(WatchListItem, WatchListItemAdmin)


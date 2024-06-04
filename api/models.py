from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    watchlist = models.ManyToManyField("api.Movie", through="api.WatchListItem")


class Rating(models.Model):

    slug = models.SlugField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):

    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=201)  # looked online to find the longest movie title
    synopsis = models.TextField()
    released_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    rating = models.ForeignKey(Rating, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class WatchListItem(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.movie} {self.user} {self.watched}"

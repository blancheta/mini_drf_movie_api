# Mini Movie API

The goal of this project is
to provide simple examples of important
features of Django Rest Framework.

1. ModelSerializer
2. Serializer
3. Validators in Serializers
4. Postman requests

# API Client can:

MOVIES:
- [X] list movies [ListApiMixin]
- [X] get a movie detail [RetrieveApiMixin]

WATCHLIST: [Viewset without Update]
- [X] add a movie in a user watchlist
- [X] delete a movie from a user watchlist
- [X] list all movies in a user watchlist

# Administrator can also:

USERS: [Viewset, permission_class isAdmin]
- [X] create a user 
- [X] update a user 
- [X] delete a user 
- [X] get details for a single user
- [X] list all users 
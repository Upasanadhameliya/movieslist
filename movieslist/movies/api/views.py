from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .serializers import MovieSerializer, ActorSerializer
from movieslist.movies.models import Movie, Actor

class MovieViewSet(ListModelMixin, GenericViewSet):
	serializer_class = MovieSerializer
	queryset = Movie.objects.all()

class ActorViewSet(ListModelMixin, GenericViewSet):
	serializer_class = ActorSerializer
	queryset = Actor.objects.all()
from rest_framework import serializers
from movieslist.movies.models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
	num_of_actors = serializers.IntegerField()

	class Meta:
		model = Movie
		fields = ('title','description','release_date','votes','num_of_actors')

class ActorSerializer(serializers.ModelSerializer):
	num_of_movies = serializers.IntegerField()

	class Meta:
		model = Actor
		fields = ('name','dob','num_of_movies')

from rest_framework import serializers
from movieslist.movies.models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('title','description','release_date','votes')

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		fields = ('name','dob')

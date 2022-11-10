from rest_framework import serializers
from movieslist.movies import Movie

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('title','description','release_date','votes')

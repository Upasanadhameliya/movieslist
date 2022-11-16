from django.db import models
from django.core.validators import MinValueValidator

class Movie(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500, blank=True, null=True)
	release_date = models.DateField(blank=True,null=True)
	votes = models.IntegerField(default=0)

	@property
	def num_of_actors(self):
		return self.cast_set.count()

	def __str__(self):
		return self.title

class Actor(models.Model):
	name = models.CharField(max_length=255)
	dob = models.DateField(null=True,blank=True)

	@property
	def num_of_movies(self):
		return self.cast_set.count()

	def __str__(self):
		return self.name

class Cast(models.Model):
	actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
	movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

	def __str__(self):
		return self.actor.name + " - " + self.movie.title
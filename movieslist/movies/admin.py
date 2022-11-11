from django.contrib import admin
from .models import Movie, Actor, Cast

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	pass

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
	pass
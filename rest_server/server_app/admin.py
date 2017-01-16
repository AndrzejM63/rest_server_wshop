from django.contrib import admin

# Register your models here.
from server_app.models import Person, Movie


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthdate')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'actors_list', 'year')

    def actors_list(self, movie):
        return ", ".join([str(t) for t in movie.actors.all()])

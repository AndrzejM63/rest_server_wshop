from rest_framework import serializers

from server_app.models import Movie, Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("pk", "name", "surname", "birthdate")


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ("title", "description", "director", "actors", "year")

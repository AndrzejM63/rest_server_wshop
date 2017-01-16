from django.shortcuts import render
from rest_framework.views import APIView, Http404, Response
from rest_framework import status

# Create your views here.
from server_app.models import Movie, Person
from server_app.serializers import PersonSerializer, MovieSerializer


class PersonView(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonListView(APIView):
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesListView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


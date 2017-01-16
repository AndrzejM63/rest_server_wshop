from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person, null=True,
                                    related_name='movie_director')
    actors = models.ManyToManyField(Person, blank=True,
                                    related_name='movie_actor')
    year = models.SmallIntegerField()

    def __str_(self):
        return self.title
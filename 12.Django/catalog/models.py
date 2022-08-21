from django.db import models


class Director(models.Model):
    first_name = models.CharField(
        max_length=64, help_text='Nombre del director:', blank=True)
    last_name = models.CharField(
        max_length=64, help_text='Apellidos director:', blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Movie(models.Model):
    title = models.CharField(
        max_length=64, help_text='Introduce el titulo de la película:')
    description = models.CharField(max_length=255, help_text='Descripción:')
    director = models.ForeignKey(
        'Director', on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return self.title

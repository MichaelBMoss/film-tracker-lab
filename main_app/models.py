from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)


class Actor(models.Model):
  name = models.CharField(max_length=50)
  gender = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('actors_detail', kwargs={'pk': self.id})


class Film(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  plot = models.TextField(max_length=250)
  year = models.IntegerField()
  actors = models.ManyToManyField(Actor)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'film_id': self.id})

  def fed_for_today(self):
    return self.director_set.filter(date=date.today()).count() >= len(MEALS)


class Director(models.Model):
  date = models.DateField('Director Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  film = models.ForeignKey(
    Film,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
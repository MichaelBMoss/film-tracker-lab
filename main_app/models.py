from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)


# Create your models here.
class Actor(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('actors_detail', kwargs={'pk': self.id})


class Film(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  # Create a M:M relationship with Actor
  # actors is the Related Manager
  actors = models.ManyToManyField(Actor)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
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
  # Create a film_id FK
  film = models.ForeignKey(
    Film,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
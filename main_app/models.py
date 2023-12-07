from django.db import models
from django.urls import reverse
from datetime import date

LOCATIONS = (
    ('N', 'New York City, NY'),
    ('L', 'Los Angeles, CA'),
    ('C', 'Chicago, IL'),
    ('H', 'Houston, TX'),
    ('P', 'Philadelphia, PA'),
    ('S', 'San Diego, CA'),
    ('D', 'Dallas, TX'),
)


class Actor(models.Model):
  name = models.CharField(max_length=50)
  nickname = models.CharField(max_length=20)

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
    return self.screening_set.filter(date=date.today()).count() >= len(LOCATIONS)
  
  def most_recent_screening(self):
    recent_screening = self.screening_set.order_by('-date').first()
    if recent_screening:
        return {'date': recent_screening.date, 'location': recent_screening.get_location_display()}
    else:
        return {'date': None, 'location': None}


class Screening(models.Model):
  date = models.DateField('Screening Date')
  location = models.CharField(
    max_length=1,
    choices=LOCATIONS,
    default=LOCATIONS[0][0]
  )

  film = models.ForeignKey(
    Film,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_location_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
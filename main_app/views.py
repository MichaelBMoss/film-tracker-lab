from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Film, Actor
from .forms import ScreeningForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def films_index(request):
  films = Film.objects.all()
  return render(request, 'films/index.html', {
    'films': films
  })

def films_detail(request, film_id):
  film = Film.objects.get(id=film_id)
  id_list = film.actors.all().values_list('id')
  actors_film_doesnt_have = Actor.objects.exclude(id__in=id_list)
  screening_form = ScreeningForm()
  return render(request, 'films/detail.html', {
    'film': film, 'screening_form': screening_form,
    'actors': actors_film_doesnt_have
  })

class FilmCreate(CreateView):
  model = Film
  fields = ['name', 'genre', 'plot', 'year']

class FilmUpdate(UpdateView):
  model = Film
  fields = ['genre', 'plot', 'year']

class FilmDelete(DeleteView):
  model = Film
  success_url = '/films'

def add_screening(request, film_id):
  form = ScreeningForm(request.POST)
  if form.is_valid():
    new_screening = form.save(commit=False)
    new_screening.film_id = film_id
    new_screening.save()
  return redirect('detail', film_id=film_id)

class ActorList(ListView):
  model = Actor

class ActorDetail(DetailView):
  model = Actor

class ActorCreate(CreateView):
  model = Actor
  fields = '__all__'

class ActorUpdate(UpdateView):
  model = Actor
  fields = ['name', 'nickname']

class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors'

def assoc_actor(request, film_id, actor_id):
  Film.objects.get(id=film_id).actors.add(actor_id)
  return redirect('detail', film_id=film_id)

def unassoc_actor(request, film_id, actor_id):
  Film.objects.get(id=film_id).actors.remove(actor_id)
  return redirect('detail', film_id=film_id)
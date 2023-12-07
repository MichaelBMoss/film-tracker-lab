from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Film, Actor
from .forms import DirectorForm

# Create your views here.
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
  # First, create a list of the actor ids that the film DOES have
  id_list = film.actors.all().values_list('id')
  # Query for the actors that the film doesn't have
  # by using the exclude() method vs. the filter() method
  actors_film_doesnt_have = Actor.objects.exclude(id__in=id_list)
  # instantiate DirectorForm to be rendered in detail.html
  director_form = DirectorForm()
  return render(request, 'films/detail.html', {
    'film': film, 'director_form': director_form,
    'actors': actors_film_doesnt_have
  })

class FilmCreate(CreateView):
  model = Film
  fields = ['name', 'breed', 'description', 'age']

class FilmUpdate(UpdateView):
  model = Film
  fields = ['breed', 'description', 'age']

class FilmDelete(DeleteView):
  model = Film
  success_url = '/films'

def add_director(request, film_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = DirectorForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # film_id FK.
    new_director = form.save(commit=False)
    new_director.film_id = film_id
    new_director.save()
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
  fields = ['name', 'color']

class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors'

def assoc_actor(request, film_id, actor_id):
  Film.objects.get(id=film_id).actors.add(actor_id)
  return redirect('detail', film_id=film_id)

def unassoc_actor(request, film_id, actor_id):
  Film.objects.get(id=film_id).actors.remove(actor_id)
  return redirect('detail', film_id=film_id)
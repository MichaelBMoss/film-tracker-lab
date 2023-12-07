from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('films/', views.films_index, name='index'),
  path('films/<int:film_id>/', views.films_detail, name='detail'),
  path('films/create/', views.FilmCreate.as_view(), name='films_create'),
  path('films/<int:pk>/update/', views.FilmUpdate.as_view(), name='films_update'),
  path('films/<int:pk>/delete/', views.FilmDelete.as_view(), name='films_delete'),
  path('films/<int:film_id>/add_screening/', views.add_screening, name='add_screening'),
  path('films/<int:film_id>/assoc_actor/<int:actor_id>/', views.assoc_actor, name='assoc_actor'),
  path('films/<int:film_id>/unassoc_actor/<int:actor_id>/', views.unassoc_actor, name='unassoc_actor'),
  path('actors/', views.ActorList.as_view(), name='actors_index'),
  path('actors/<int:pk>/', views.ActorDetail.as_view(), name='actors_detail'),
  path('actors/create/', views.ActorCreate.as_view(), name='actors_create'),
  path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actors_update'),
  path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actors_delete'),
]
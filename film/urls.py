from django.urls import path

from . import views

app_name = 'film' 

urlpatterns = [
     path("", views.homepage_view, name="homepage"),
     
     path('ajouter_commentaire/<int:film_id>/', views.ajouter_commentaire, name='ajouter_commentaire'),
     
     path('creer_collection/', views.creer_collection, name='creer_collection'),
    path('liste_collections/', views.liste_collections, name='liste_collections'),
    path('supprimer_collection/<str:nom>/', views.supprimer_collection, name='supprimer_collection'),

     path('ajouter_film/<int:film_id>/', views.ajouter_film, name='ajouter_film'),
    path('liste_films_panier/', views.liste_films_panier, name='liste_films_panier'),
    path('supprimer_films_panier/<int:film_id>/', views.supprimer_film_panier, name='supprimer_film_panier'),
    
     path('<int:film_id>/', views.film_detail, name='film_detail'),
     path('search/', views.search, name='movie_search'),
]

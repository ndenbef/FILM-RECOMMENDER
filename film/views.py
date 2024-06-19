from django.contrib import messages
from urllib import response
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .api import get_movies, get_movies_details, add_movies
from .forms import CollectionCreationForm, RatingForm
from .models import FilmSerie, Panier, Collection, Comment, Rating
from.recommender import movie_recommender, user_movie_recommender

from django.db.models import Avg


import requests
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def homepage_view(request):
    # add_movies()
    films = FilmSerie.objects.all().order_by('note')

    
    # nombre d'éléments par page
    elements_par_page = 106

    # créer un objet Paginator avec la liste et le nombre d'éléments par page
    paginator = Paginator(films, elements_par_page)

    # obtenir le numéro de page à afficher
    page = request.GET.get('page')
    
    print(page)

    try:
        # obtenir les éléments pour la page courante
        elements = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an interger, deliver first page.
        elements = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        elements = paginator.page(paginator.num_pages)
        
    print(elements)

    
    # return HttpResponse("Hello you are late you better hurry up !")
    return render(request, "film/base.html", {'films': films, 'elements': elements})

def film_detail(request, film_id):
    # add_movies()
    personal = user_movie_recommender(request)
    print(personal)
    
    movie = get_object_or_404(FilmSerie, id=film_id)
    
    film = get_movies_details(film_id)
    films = FilmSerie.objects.get(title = film['title'])
    comments =Comment.objects.filter(film=movie)
    
    movie = get_object_or_404(FilmSerie, id=film_id)
    recommendations = movie_recommender(film_id)
    print("-----------------------------       NEXT    ----------------------------------------")
    print(recommendations)
    
    user_rating = Rating.objects.filter(user=request.user, film=movie).first()

    if user_rating:
        form = RatingForm({'stars': user_rating.stars})
    else:
        form = RatingForm()

    average_rating = movie.ratings.aggregate(Avg('stars'))['stars__avg']
    
    context = {
        'movie': movie,
        'film' : film,
        'comments': comments,
        'recommendations': recommendations,
        'personals': personal
    }

    
    return render(request, 'film/detail.html', context)

def search(request):
    if request.method == 'GET':
        form = request.GET.get('search')

        if form:
            # query = form.cleaned_data['query']
            films = FilmSerie.objects.filter(title__icontains=form)
            #movie = get_object_or_404(FilmSerie, id=films['id'])
            # recommendations = movie_recommender(films.get(id))
            # for film in films:
            #     movie = get_object_or_404(FilmSerie, id=film.id)
            #     recommendations = movie_recommender(film.id)

            return render(request, 'film/result.html', {'movies': films, 'form': form})
        else:
            films = FilmSerie.objects.all()
        
            # return HttpResponse("Hello you are late you better hurry up !")
            return render(request, "film/base.html", {'films': films})
        
@login_required
def ajouter_film(request, film_id):
    film = FilmSerie.objects.get(id=film_id)
    panier, _ = Panier.objects.get_or_create(user=request.user)
    panier.films.add(film)
    messages.success(request, f"{film.title} a été ajouté à votre panier.")
    return redirect('film:liste_films_panier')

@login_required
def liste_films_panier(request):
    panier_exists = Panier.objects.filter(user=request.user).exists()
    if not panier_exists:
        panier = Panier.objects.create(user=request.user)
    else:
        panier = Panier.objects.get(user=request.user)

    liste_films = panier.films.all()
    context = {'liste_films': liste_films}
    return render(request, 'film/panier.html', context)

@login_required
def supprimer_film_panier(request, film_id):
    
    movie = get_object_or_404(FilmSerie, id=film_id)
    print("panier_1")
    
    if request.method == "POST":
        print("panier_2")
        panier = Panier.objects.get(user=request.user)
        if not request.user == panier.user:
            return HttpResponseForbidden()
        
        film_exists = panier.films.filter(id=film_id).first()
        if film_exists:
            print("panier_3")
            panier.films.remove(movie)
            messages.success(request, f"{movie.title} a été supprimé du panier.")
        else:
            messages.error(request, f"{movie.title} n'est pas dans le panier.")


    return redirect('film:liste_films_panier')

@login_required
def creer_collection(request):
    print("collec_1")
    panier = Panier.objects.get(user=request.user)
    print("collec_2")
    if request.method == 'POST':
        print("collec_3")
        nom = request.POST.get('nom_collection')
        success = False

        
        if Collection.objects.filter(user=request.user, nom=nom).exists():
            message = 'Vous avez déjà créé une collection avec ce nom.'
        else:

            films = panier.films.all()
            collection = Collection.objects.create(user=request.user, nom=nom)
            print("collec_4")
            for film in films:
                collection.films.add(film)
                print("collec_5")
            
            print("collec_6")
            panier.films.clear()
            print("collec_7")
            success = True
            messages.success(request, f"Collection {nom} créée avec succès !")
            print("collec_8")
            return redirect('film:liste_collections')
    else:
        messages.error(request, "Veuillez entrer un nom de collection valide.")
    print("collec_9")

    context = {'panier': panier, 'success': success, 'message': message}
    return render(request, 'film/collection.html', context)

@login_required
def liste_collections(request):
    collections = Collection.objects.filter(user=request.user)
    context = {'collections': collections}
    return render(request, 'film/collection.html', context)

@login_required
def supprimer_collection(request, nom):
    collection = Collection.objects.filter(user=request.user, nom=nom).first()
    if not request.user == collection.user:
        return HttpResponseForbidden()
    collection.delete()
    messages.success(request, f"Collection {collection.nom} supprimée avec succès.")
    return redirect('film:liste_collections')


@login_required
def ajouter_commentaire(request, film_id):
    movie = get_object_or_404(FilmSerie, id=film_id)
    parent_comment_id = request.POST.get('parent_comment_id') 

    if request.method == 'POST':
        content = request.POST.get('commentaire')
        parent_comment = None
        if parent_comment_id:
            parent_comment = Comment.objects.get(id=parent_comment_id)
        Comment.objects.create(user=request.user, film=movie, content=content, parent_comment=parent_comment)
        messages.success(request, 'Votre commentaire a été ajouté avec succès.')
        return redirect('film:film_detail', film_id=film_id)

    context = {
        'film': movie,
        'form': content,
    }
    return render(request, 'film/detail.html', context)

@login_required
def ajouter_note(request, film_id):
    film = get_object_or_404(FilmSerie, id=film_id)
    user_rating = Rating.objects.filter(user=request.user, film=film).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            stars = form.cleaned_data['stars']

            if user_rating:
                user_rating.stars = stars
                user_rating.save()
            else:
                Rating.objects.create(user=request.user, film=film, stars=stars)

            messages.success(request, 'Votre note a été enregistrée.')
            return redirect('film:detail_film', film_id=film_id)
    else:
        if user_rating:
            form = RatingForm({'stars': user_rating.stars})
        else:
            form = RatingForm()

    context = {
        'film': film,
        'form': form,
    }
    return render(request, 'film/ajouter_note.html', context)

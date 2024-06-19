from django.contrib import admin

from film.models import FilmSerie, Utilisateur

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(FilmSerie)



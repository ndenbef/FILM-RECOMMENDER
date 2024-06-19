from django.db import models
from registration.models import User

class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    nomut = models.CharField(max_length=50)
    ageut = models.IntegerField()
    code = models.CharField(max_length=50)
    genreut = models.CharField(max_length=50)
    role = models.CharField(max_length=2)
    date_ut = models.DateField()
    

class FilmSerie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, null=True, default="Unavailable")
    datef = models.DateField(null=True)
    langue = models.CharField(max_length=10, null=True)
    j_aime = models.IntegerField(null=True, default=0)
    j_aime_pas = models.IntegerField(null=True, default=0)
    note = models.DecimalField(max_digits=3, decimal_places=1, null=True, default=0)
    poster_path = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    films = models.ManyToManyField(FilmSerie, related_name='panier')
    
    
    
class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    films = models.ManyToManyField(FilmSerie)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'nom')
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(FilmSerie, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


    def __str__(self):
        return f"{self.user.username} - {self.film.titre}"
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(FilmSerie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(default=0, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'film',)
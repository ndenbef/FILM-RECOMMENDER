from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import User


class CustomUserCreationForm(UserCreationForm): 
    GENRE_CHOICES1 = ( 
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Fantasy', 'Fantasy'),
        ('ScienceFiction', 'Science Fiction'),
        ('Crime', 'Crime'),
        ('Drama', 'Drama'),
        ('Thriller', 'Thriller'),
        ('Animation', 'Animation'),
        ('Family', 'Family'),
        ('Western', 'Western'),
 )
    
    GENRE_CHOICES2 = ( 
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Mystery', 'Mystery'),
        ('History', 'History'),
        ('War', 'War'),
        ('Music', 'Music'),
        ('Documentary', 'Documentary'),
        ('Foreign', 'Foreign'),
        ('TVMovie', 'TV Movie'),
 ) 


    
     
    AGE_CHOICES = [(i, str(i)) for i in range(10, 91)]
    
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter First name', 'size': '44'})) 
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter First name', 'size': '44'})) 
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'size': '44'})) 
    age = forms.ChoiceField(required=False,choices=AGE_CHOICES, widget=forms.Select(attrs={'placeholder': 'Choose an age', 'size': '1', 'width': '150', 'padding': '10'})) 
    genre1 = forms.MultipleChoiceField(choices=GENRE_CHOICES1, widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre-field'})) 
    genre2 = forms.MultipleChoiceField(choices=GENRE_CHOICES2, widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size': '44'})) 
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Verify Password', 'size': '44'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'age', 'genre1', 'genre2', 'password')
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prénom',
            'username': 'Email',
            'age': 'Âge',
            'genre1': 'Genres',
            'genre2': '',
            'password': 'Mot de passe',
            # 'password2': 'Confirmer mot de passe'
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['genre'].widget.attrs.update({'id': 'genre-field'})

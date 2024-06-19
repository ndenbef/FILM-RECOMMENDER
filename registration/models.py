from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser): 
    # nom = models.CharField(max_length=50, null=True, blank=True) 
    # prenom = models.CharField(max_length=50, null=True, blank=True) 
    # email = models.EmailField(max_length=100, unique=True) 
    age = models.IntegerField(null=True, blank=True) 
    genre1 = models.CharField(max_length=256, blank=True) 
    genre2 = models.CharField(max_length=256, blank=True)
    # panier = models.ManyToManyField(Panier, blank=True)
    
    user_permissions = models.ManyToManyField(Permission, blank=True)
    
    groups = models.ManyToManyField(Group, related_name='registration_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='registration_user_permissions',
        blank=True, 
    )

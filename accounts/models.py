from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, date
import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

# Create your models here.


class Profil(models.Model):
    PROFILE_CHOICES = (
        ('createur', 'createur'),
        )
    
    GENRE_CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Other', 'Other'),
        ('None', 'None'),
        )

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True)
    lastname = models.CharField(max_length=45, blank=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255,blank=True, null=True)
    bithrDay = models.DateField(default=date.today, null=True)
    created_date = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    adress = models.CharField(max_length=254, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)    
    photo=models.FileField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        

    def __str__(self) :
        return str(self.user)

class Account(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Nom")
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    username = models.CharField(max_length=50, unique=True, verbose_name="Nom d'utilisateur")
    email = models.EmailField(unique=True, verbose_name="Email")
    code_postal = models.CharField(max_length=10, verbose_name="Code Postal")
    adresse = models.TextField(verbose_name="Adresse")
    sexe = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sexe")
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)    
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False) 
    activation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    
class PasswordResetToken(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token


# class TemporaryAccount(models.Model):
#     username = models.CharField(max_length=255)  # ajoutez tous les autres champs nécessaires ici
#     email = models.EmailField()
#     password = models.CharField(max_length=255)  # assurez-vous de stocker ceci de manière sécurisée
#     activation_code = models.CharField(max_length=6)
#     timestamp = models.DateTimeField(auto_now_add=True)  # pour suivre quand il a été créé

class TemporaryAccount(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Assurez-vous de stocker ceci de manière sécurisée
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=10, choices=[('M', 'M'), ('F', 'F')])
    code_postal = models.CharField(max_length=10)
    adresse = models.TextField()
    activation_code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.username

# class Events(models.Model):
#     title=models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     nbre_place= models.IntegerField( blank=True, default=0)
#     date=models.CharField( max_length=255)
#     designation=models.CharField(max_length=255, blank=True)
#     photo=models.ImageField( upload_to='photos/%Y/%m/%d/')
#     is_featured = models.BooleanField(default=False, null=True , blank=True)
#     last_model = models.BooleanField(default=False, null=True , blank=True)
#     created_date = models.DateField(auto_now_add=True)
#     attendees = models.ManyToManyField(Account, related_name="reserved_events", blank=True)
    
#     def reserve_event(self, account):
#         comparison_date = datetime.strptime("2023-12-31", "%Y-%m-%d").date()
#         if self.nbre_place < 100 and datetime.strptime(self.date, "%Y-%m-%d").date() < comparison_date:
#             self.nbre_place += 1
#             self.attendees.add(account)
#             self.save()
#             return True
#         return False

#     def __str__(self):
#         return self.title
    
# class ReserveEvent(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
#     reserved_on = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         if not self.event.reserve_event(self.account):
#             raise ValidationError("Can't reserve this event.")
#         super(ReserveEvent, self).save(*args, **kwargs)

#     def __str__(self):
#         return str(self.event) + " "+  str(self.account) + " "+ str(self.reserved_on)
        

class Evenement(models.Model):
    name_artist = models.CharField(max_length=255, verbose_name="Nom de l'artiste")
    price_artist = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix de l'événement")
    nbre_place_artist = models.IntegerField(blank=True, default=0, verbose_name="Nombre de places disponibles")
    date_start = models.DateTimeField(verbose_name="Date et heure de début de l'événement")
    date_end = models.DateTimeField(verbose_name="Date et heure de fin de l'événement")
    designation_artist = models.CharField(max_length=255, blank=True, verbose_name="Description de l'artiste")
    photo_artist = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Photo de l'artiste")
    is_featured_artist = models.BooleanField(default=False, null=True, blank=True, verbose_name="En vedette")
    last_model_artist = models.BooleanField(default=False, null=True, blank=True, verbose_name="Dernier modèle")
    created_date_artist = models.DateField(auto_now_add=True, verbose_name="Date de création")
    url_youtube=models.CharField(max_length=255,verbose_name="URL Youtube")
    attendees = models.ManyToManyField(Account, related_name="reserve", blank=True)

    def __str__(self):
        return self.name_artist

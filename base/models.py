from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, date
# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    name = models.CharField( max_length=45, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    decription = models.TextField( max_length=1000, blank=True)
    quantites = models.IntegerField( blank=True, default=0)
    categorie = models.CharField( max_length=45, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ": €" + str(self.prix)

class Magasin(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    nom = models.CharField(max_length=45, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    adresse = models.CharField(max_length=45, blank=True)
    telephone = models.CharField(max_length=45, blank=True)
    prod = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, related_name='prod')

    def __str__(self):
        return str(self.name) + ": " + str(self.adresse)

class Article(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    title_art = models.CharField( max_length=45, blank=True)
    content_art = models.TextField( max_length=1000, blank=True)
    created_date_art = models.DateField(auto_now_add=True)
    update_date_art = models.DateField(default=date.today, null=True)
    user_art = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title) + str(self.user)

class Response(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    title_resp = models.CharField( max_length=45, blank=True)
    message_resp = models.TextField( max_length=1000, blank=True)
    created_date_resp = models.DateField(auto_now_add=True)
    update_date_resp = models.DateField(default=date.today, null=True)
    user_resp = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article_resp = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title_resp) + str(self.user)
    
class Events(models.Model):
    title=models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    nbre_place= models.IntegerField( blank=True, default=0)
    date=models.CharField( max_length=255)
    designation=models.CharField(max_length=255, blank=True)
    photo=models.ImageField( upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False, null=True , blank=True)
    last_model = models.BooleanField(default=False, null=True , blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
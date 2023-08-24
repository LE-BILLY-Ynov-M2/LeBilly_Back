# troc-your-diy-back
Back-end for Troc Your DIY Ydays Project

Pour tester l'API il faut devoir faire ceci:
Cloner le projet ensuite
    1-Intaller Django
    2-pip install django
    3-python manage.py runserver 5500
    4-http://127.0.0.1:5500/api_schema

Pour acceder au lien Swagger: "http://127.0.0.1:5500/api_schema"

Voici les profiles existants
    PROFILE_CHOICES = (
        ('createur', 'createur'),
        )
Le genre pour le choice 
    GENRE_CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Other', 'Other'),
        ('None', 'None'),
        )# LeBilly_Back

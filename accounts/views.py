from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Account
from .serializers import AccountSerializer
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer
from rest_framework import serializers
import random
from rest_framework.views import APIView
from django.contrib.auth import authenticate
import cloudinary.uploader
from django.http import JsonResponse
import cloudinary.api
from cloudinary.api import resources
from rest_framework import generics
from django.shortcuts import get_object_or_404
import stripe
stripe.api_key = "sk_test_51LuypqEMbpaxmGP6WCG43ONNmFMRfyKuOxPihh9OU3UJVYc72zAyV0oU7KmQCcjclpdNemi6kbP9c7aNyeWgW5Hh00jCTh8xsV"

#from home.models import Demande, BanqueImange, BanqueImangePhoto, BanqueRessource
#from contacts.models import Contact

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in.')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid login credentials')
#             return redirect('login')
#     return render(request, 'accounts/login.html')

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists!')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'Email already exists!')
#                     return redirect('register')
#                 else:
#                     user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
#                     auth.login(request, user)
#                     messages.success(request, 'You are now logged in.')
#                     return redirect('home')
#                     user.save()
#                     messages.success(request, 'You are registered successfully.')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Password do not match')
#             serailizer = ProfilSerializer(user, many=True)
#             return Response(serailizer.data)
#     else:
#         serailizer = ProfilSerializer(user, many=True)
#         return Response(serailizer.data)

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     print(data)
#     print("data['username']",data['username'],"password=data['password']",data['password'])
#     try:
#         user = Profil.authenticate(username=data['username'], password=data['password'])
#         #print("user",user)
#         #user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             print("OK")
#             message = {'detail': 'You are now logged in.'}
#             print("T1")
#         else:
#             message = {'detail': 'Invalid login credentials'}
#             print("T2")
#     except:
#         message = {'detail': 'Un petit soucis'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     print(data)
#     profile = Profil.objects.filter(username=data['username'],password=data['password'])
#     print("profile",profile)
    
#     serializer = ProfilSerializer(profile, many=False)
#     return Response(serializer.data)



# @api_view(['POST'])
# def create_account(request):
#     if request.method == 'POST':
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_account(request):
#     if request.method == 'POST':
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data['is_active'] = True
#             user = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @api_view(['POST'])
# def create_account(request):
#     if request.method == 'POST':
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            activation_code = str(random.randint(100000, 999999))

            temp_account = TemporaryAccount(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
                name=serializer.validated_data["name"],
                prenom=serializer.validated_data["prenom"],
                sexe=serializer.validated_data["sexe"],
                code_postal=serializer.validated_data["code_postal"],
                adresse=serializer.validated_data["adresse"],
                activation_code=activation_code
            )

            temp_account.save()

            activate_link = f"http://127.0.0.1:3000/verifCode?{temp_account.id}"
            send_mail(
                'Activate your account',
                f'Cliquer sur ce lien: {activate_link}. '
                f'Code d\'activation: {activation_code}.',
                'mamerane1003@gmail.com',
                [temp_account.email],
                fail_silently=False,
            )

            response_data = {
                "message": "Un email vous a été envoyé pour terminer votre inscription."
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def activate_account(request, temp_account_id):
    try:
        temp_account = TemporaryAccount.objects.get(id=temp_account_id)
        entered_code = request.data.get("activation_code")

        if not entered_code:
            return Response({"error": "Activation code is required."}, status=status.HTTP_400_BAD_REQUEST)

        if temp_account.activation_code == entered_code:
            
            new_account = Account(
                username=temp_account.username,
                email=temp_account.email,
                password=temp_account.password,
                name=temp_account.name,
                prenom=temp_account.prenom,
                sexe=temp_account.sexe,
                code_postal=temp_account.code_postal,
                adresse=temp_account.adresse
            )

            new_account.save()
            temp_account.delete()

            return Response({"message": "Code activer avec succées!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Code Invalid."}, status=status.HTTP_400_BAD_REQUEST)

    except TemporaryAccount.DoesNotExist:
        return Response({"error": "Lien Invalid."}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
def verify_token(request, token):
    try:
        account = Account.objects.get(token=token)
        return Response({"detail": "Token valide."}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({"detail": "Token invalide ou inexistant."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_account(request, id):
    try:
        user = Account.objects.get(pk=id)
        print("user",user)
    except Account.DoesNotExist:
        return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

    # Mettez à jour les champs
    for field, value in request.data.items():
        setattr(user, field, value)
    user.save()

    return Response({'message': 'Utilisateur mis à jour avec succès',
                     "user_id": user.id,"token": user.token}, status=status.HTTP_200_OK)


class AccountListView(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class EventsListView(APIView):
#     def get(self, request, *args, **kwargs):
#         events = Events.objects.all()
#         print("event",events)
#         serializer = EventsSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class GetUserView(APIView):
    def get(self, request, id):
        try:
            user = Account.objects.get(pk=id)
            serializer = AccountSerializer(user)  # Utilisez votre sérialiseur pour transformer l'objet utilisateur en JSON
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"detail": "L'utilisateur n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_admin_user(request):
    
    if not request.user.is_staff:
        return Response({"detail": "Vous n'avez pas les autorisations nécessaires pour créer un administrateur."}, status=status.HTTP_403_FORBIDDEN)
    data = request.data

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        is_staff=True,
    )

    account = Account.objects.create(
        name=data['name'],
        prenom=data['prenom'],
        email=data['email'],
        code_postal=data['code_postal'],
        adresse=data['adresse'],
        sexe=data['sexe'],
        token=data['token'],
        activation_token=data['activation_token'],
        is_active=True,
    )


    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_admin_user(request, id):
    if not request.user.is_staff:
        return Response({"detail": "Vous n'avez pas les autorisations nécessaires pour modifier un administrateur."}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(id=id)

        data = request.data

        user.username = data['username']
        user.set_password(data['password'])
        user.save()

        account = Account.objects.get(user=user)
        account.name = data['name']
        account.prenom = data['prenom']
        account.email = data['email']
        account.code_postal = data['code_postal']
        account.adresse = data['adresse']
        account.sexe = data['sexe']
        account.token = data['token']
        account.activation_token = data['activation_token']
        account.is_active = data['is_active']
        account.save()

        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"detail": "L'utilisateur administrateur spécifié n'existe pas."}, status=status.HTTP_404_NOT_FOUND)


# def delete_user(request, user_id):
#     try:
#         # Rechercher l'utilisateur par son ID
#         user = Account.objects.get(pk=user_id)
#         user.delete()  # Supprimer l'utilisateur
#         return JsonResponse({"message": "Utilisateur supprimé avec succès."})
#     except Account.DoesNotExist:
#         return JsonResponse({"error": "L'utilisateur n'existe pas."}, status=404)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

# class DeleteUserView(APIView):
#     def post(self, request):
#         try:
#             user_id = request.data.get('user_id') 

#             user = Account.objects.get(pk=user_id)
#             return Response({"message": "Utilisateur supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
#         except Account.DoesNotExist:
#             return Response({"detail": "L'utilisateur n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteUserView(APIView):
    def delete(self, request, id):
        try:
            user = Account.objects.get(pk=id)            
            user.delete()
            return Response({"message": "Utilisateur supprimé avec succès.",
                             "user_id": user.id},
                            status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response({"detail": "L'utilisateur n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['POST'])
# def reserve_event(request):
#     serializer = ReserveEventSerializer(data=request.data)
#     print("serializer",serializer)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def upload_photo_user(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            result = cloudinary.uploader.upload(
                uploaded_file,
                folder="photos"
            )
            if result:
                return JsonResponse(result, status=200)
            else:
                return JsonResponse({"message": "Upload failed"}, status=500)
        else:
            return JsonResponse({"message": "Vous devez choisir une image"}, status=500)
    return JsonResponse({"message": "Invalid request"}, status=400)

def delete_photo_user(request, user_id):
    if request.method == "DELETE":
        result = cloudinary.uploader.destroy(f"users/{user_id}")
        if result.get("result") == "ok":
            return JsonResponse({"message": "delete ok"}, status=200)
        else:
            return JsonResponse({"error": "error delete"}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)
# views.py

def get_all_photos(request):
    if request.method == "GET":
        results = cloudinary.api.resources(type="upload", prefix="Photos_LeBily/")
        return JsonResponse(results, safe=False)
    return JsonResponse({"error": "Invalid request"}, status=400)

@api_view(['GET'])
def get_images(request):
    cloudinary.config(
        cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
        api_key = settings.CLOUDINARY_STORAGE['API_KEY'],
        api_secret = settings.CLOUDINARY_STORAGE['API_SECRET']
    )

    images_list = resources(prefix="Photos_LeBilly/", type="upload")
    urls = [image['url'] for image in images_list['resources']]

    return JsonResponse({'images': urls})


class GetEventById(generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class GetAllEvents(generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class StripePayment(APIView):
    def post(self, request, event_id):
        event = get_object_or_404(Evenement, pk=event_id)
        token = request.data.get('token')
        try:

            charge = stripe.Charge.create(
                amount=int(event.price_artist * 100),  
                currency='usd',
                source=token,
                description='Payment for Event: {}'.format(event.name_artist),
            )

            return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['id', 'name', 'prenom', 'username', 'email', 'code_postal', 'adresse', 'sexe']

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_account(request):
#     try:
#         user = request.user.id

#         serializer = AccountSerializer(user, data=request.data, partial=True) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Account.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
# @login_required
# @api_view(['POST'])
# def login_view(request):
#     username_or_email = request.data.get('username')
#     password = request.data.get('password')

#     if not username_or_email or not password:
#         return Response({"detail": "Les champs 'username' et 'password' sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = None
#         if '@' in username_or_email:
#             user = Account.objects.get(email=username_or_email)
#         else:
#             user = Account.objects.get(username=username_or_email)
        
#         if user.check_password(password):              
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "Mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
#     except Account.DoesNotExist:
#         return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def password_reset_request(request):
    email = request.data.get('email')
    user = Account.objects.filter(email=email).first()
    if not user:
        return Response({"detail": "E-mail non trouvé."}, status=status.HTTP_404_NOT_FOUND)

    token = PasswordResetToken.objects.create(user=user)
    reset_url = f"{request.scheme}://localhost:3000/accounts/reset-password/{token.token}/"

    send_mail(
        'Réinitialisation du mot de passe',
        f'Pour réinitialiser votre mot de passe, veuillez cliquer sur le lien suivant : {reset_url}',
        settings.EMAIL_HOST_USER,
        [user.email],
    )

    return Response({"detail": "E-mail envoyé."})

@api_view(['POST'])
def password_reset(request, token):
    new_password = request.data.get('new_password')
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return Response({"detail": "Token invalide."}, status=status.HTTP_400_BAD_REQUEST)

    user = reset_token.user
    user.set_password(new_password)
    user.save()

    reset_token.delete() 

    return Response({"detail": "Mot de passe réinitialisé."})

class LoginSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    username_or_email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    token = serializers.CharField(required=False)

    def validate(self, data):
        if not data.get('token') and not (data.get('user_id') or (data.get('username_or_email') and data.get('password'))):
            raise serializers.ValidationError("Vous devez fournir un token, un user_id ou un username et password.")
        return data

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login_view(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     if not email or not password:
#         return Response({"detail": "Les champs 'email' et 'password' sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = Account.objects.get(email=email, password=password)
#         return Response({'message': "Utilisateur connecté avec succès."}, status=status.HTTP_200_OK)

#     except Account.DoesNotExist:
#         return Response({"detail": "Combinaison email/mot de passe incorrecte."}, status=status.HTTP_404_NOT_FOUND)

# @permission_classes([AllowAny]) 
# @api_view(['POST'])
# def login_view(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     if not email or not password:
#         return Response({"detail": "Les champs 'email' et 'password' sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

#     user = authenticate(request, username=email, password=password)


    # if user is not None:
    #     return Response({
    #         "message": "Utilisateur connecté avec succès.",
    #         "user_id": user.id,
    #         "token": user.token,
    #         "admin": user.is_active
    #     }, status=status.HTTP_200_OK)
#     else:
#         return Response({"detail": "Combinaison email/mot de passe incorrecte."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"detail": "Les champs 'email' et 'password' sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Account.objects.get(email=email, password=password)
        if user is not None:
            return Response({
            "message": "Utilisateur connecté avec succès.",
            "user_id": user.id,
            "token": user.token,
            "admin": user.is_active
        }, status=status.HTTP_200_OK)
        
        return Response({'message': "Utilisateur connecté avec succès."}, status=status.HTTP_200_OK)

    except Account.DoesNotExist:
        return Response({"detail": "Combinaison email/mot de passe incorrecte."}, status=status.HTTP_404_NOT_FOUND)


# @login_required
# @api_view(['POST'])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     token_key = serializer.validated_data.get('token')
#     user_id = serializer.validated_data.get('user_id')

#     # Si un token est fourni, essayez de l'authentifier
#     if token_key:
#         try:
#             token = Token.objects.get(key=token_key)
#             return Response({'token': token.key, 'user_id': token.user.id}, status=status.HTTP_200_OK)
#         except Token.DoesNotExist:
#             return Response({"detail": "Token invalide."}, status=status.HTTP_401_UNAUTHORIZED)

#     if user_id:
#         try:
#             user = Account.objects.get(id=user_id)
#         except Account.DoesNotExist:
#             return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

#     else:
#         username_or_email = serializer.validated_data['username_or_email']
#         try:
#             if '@' in username_or_email:
#                 user = Account.objects.get(email=username_or_email)
#             else:
#                 user = Account.objects.get(username=username_or_email)
#         except Account.DoesNotExist:
#             return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

#     if user.check_password(serializer.validated_data['password']):            
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
#     else:
#         return Response({"detail": "Mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         print("data",data)

#         serializer = UserSerializerWithToken(self.user).data
#         print("ser",serializer)
#         for k, v in serializer.items():
#             data[k] = v

#         return data


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
    
# @api_view(['POST'])
# def registerUser(request):
#     data = request.data
#     print("data", data)
#     try:
#         user = User.objects.create(
#             username=data['username'],
#             email=data['email'],
#             password=make_password(data['password']),
#             phone=data['phone'],
#             telephone=data['telephone'],
#             name=data['name']
#         )
#         # Set additional fields like phone and telephone if they're provided
#         # user.phone = data.get('phone', '')
#         # user.telephone = data.get('telephone', '')
#         user.save()
#         print(user)

#         serializer = UserSerializerWithToken(user, many=False)
#         return Response(serializer.data)
#     except:
#         message = {'detail': 'User with this email already exists'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def registerProfil(request):
#     data = request.data
#     user = request.user
#     print(data)
#     print("user",user)
#     try:
#         profil = Profil.objects.create(
#             user=user,
#             firstname=data['firstname'], 
#             lastname=data['lastname'],
#             genre=data['genre'],
#             bithrDay=data['bithrDay'],
#             country=data['country'],
#             code=data['code'],
#             adress=data['adress'],
#             telephone=data['telephone'],
#             profile=data['profile'],
#             photo=data['photo'])
#         profil.save()
#         serializer = ProfilSerializer(profil, many=False)
#         return Response(serializer.data)

#     except:
#         message = {'detail': 'We have a Problem with the profile'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def updateProfil(request,pk):
#     profil = Profil.objects.get(id=pk)
#     data = request.data
#     print(data)
#     print("user",profil)
#     profil.firstname=data['firstname'] 
#     profil.lastname=data['lastname']
#     profil.genre=data['genre']
#     profil.bithrDay=data['bithrDay']
#     profil.country=data['country']
#     profil.code=data['code']
#     profil.adress=data['adress']
#     profil.telephone=data['telephone']
#     profil.profile=data['profile']
#     profil.photo=data['photo']

#     profil.save()
#     serializer = ProfilSerializer(profil, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# #@permission_classes([IsAuthenticated])
# def updateUserPassword(request):
#     user = request.user
#     serializer = UserSerializerWithToken(user, many=False)

#     data = request.data
#     user.first_name = data['name']
#     user.username = data['email']
#     user.email = data['email']

#     if data['password'] != '':
#         user.password = make_password(data['password'])

#     user.save()

#     return Response(serializer.data)


# @api_view(['GET'])
# #@permission_classes([IsAuthenticated])
# def getUser(request):
#     user = request.user
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# #@permission_classes([IsAdminUser])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# #@permission_classes([IsAdminUser])
# def getUserById(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# #@permission_classes([IsAuthenticated])
# def updateUser(request, pk):
#     user = User.objects.get(id=pk)

#     data = request.data
#     print(data)

#     user.first_name = data['name']
#     user.username = data['email']
#     user.email = data['email']
#     user.is_staff = data['isAdmin']
#     if data['password'] != '':
#         user.password = make_password(data['password'])

#     user.save()

#     serializer = UserSerializer(user, many=False)

#     return Response(serializer.data)


# @api_view(['DELETE'])
# #@permission_classes([IsAdminUser])
# def deleteUser(request, pk):
#     userForDeletion = User.objects.get(id=pk)
#     userForDeletion.delete()
#     return Response('User was deleted')

   
# # @api_view(['GET'])
# # def getUserProfile(request):
# #     profile = Profil.objects.all()
# #     serializer = ProfilSerializer(profile, many=True)
# #     return Response(serializer.data)

# # @api_view(['GET'])
# # def getProfileById(request,id):
# #     profile = Profil.objects.get(pk=id)
# #     serializer = ProfilSerializer(profile, many=False)
# #     return Response(serializer.data)


# # @api_view(['GET'])
# # def getUsers(request):
# #     #print("data['username']",data['username'],"password=data['password']",data['password'])
# #     try:
# #         profil = Profil.objects.all()
# #         print("profil",profil)

# #     except:
# #         message = {'detail': 'On peut pas recup les users'}
# #         return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def register(request):
#     data = request.data
#     print(data)
#     try:
#         if data['password'] == data['confirm_password']:
#             print("Ok")
#             if Profil.objects.filter(username=data['username']).exists():
#                 messages.error(request, 'Username already exists!')
#                 print("Test")
#             else:
#                 if Profil.objects.filter(email=data['email']).exists():
#                     messages.error(request, 'Email already exists!')
#                      #return redirect('register')
#                     #print("Test")
#                 else:
#                     #print("01")
#                     #print("data",data['firstname'])
#                     user = Profil.objects.create(
#                         user=user,
#                         firstname=data['firstname'], 
#                         lastname=data['lastname'], 
#                         email=data['email'], 
#                         username=data['username'], 
#                         password=data['password'],
#                         confirm_password=data['confirm_password'])
#                     user.save()
#                     serializer = ProfilSerializer(user, many=False)
#                     return Response(serializer.data)
#     except:
#         message = {'detail': 'User with this email already exists'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    
# @login_required(login_url = 'login')
# def home(request):


#     return render(request, 'accounts/home.html')



# def logout_views(request):
#     auth.logout(request)
#     return redirect('home')





from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Events
        fields = '__all__'

class ReserveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveEvent
        fields = ['account', 'event']

# class UserSerializer(serializers.ModelSerializer):
#     _id = serializers.SerializerMethodField(read_only=True)
#     isAdmin = serializers.SerializerMethodField(read_only=True)
#     name = serializers.CharField(source='get_full_name', read_only=True)
#     phone = serializers.CharField(write_only=True)  # You might want to change the field type
#     telephone = serializers.CharField(write_only=True)  # You might want to change the field type

#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'isAdmin', 'name', 'phone', 'telephone']

#     def get__id(self, obj):
#         return obj.id

#     def get_isAdmin(self, obj):
#         return obj.is_staff

# class UserSerializerWithToken(UserSerializer):
#     token = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'isAdmin', 'name', 'phone', 'telephone', 'token']

#     def get_token(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token.access_token)
    

# class UserSerializer(serializers.ModelSerializer):
#     #name = serializers.SerializerMethodField(read_only=True)
#     #profession = serializers.SerializerMethodField(read_only=True)
#     _id = serializers.SerializerMethodField(read_only=True)
#     isAdmin = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'isAdmin']

#     def get__id(self, obj):
#         return obj.id

#     def get_isAdmin(self, obj):
#         return obj.is_staff




# class UserSerializerWithToken(UserSerializer):
#     token = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'isAdmin', 'token']

#     def get_token(self, obj):
#         token = RefreshToken.for_user(obj)
#         return str(token.access_token)



# @api_view(['PUT'])
# #@permission_classes([IsAuthenticated])
# def updateUserProfile(request):
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
# def getUserProfile(request):
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

#     user.first_name = data['name']
#     user.username = data['email']
#     user.email = data['email']
#     user.is_staff = data['isAdmin']

#     user.save()

#     serializer = UserSerializer(user, many=False)

#     return Response(serializer.data)


# @api_view(['DELETE'])
# #@permission_classes([IsAdminUser])
# def deleteUser(request, pk):
#     userForDeletion = User.objects.get(id=pk)
#     userForDeletion.delete()
#     return Response('User was deleted')


# class ProfilSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  Profil
#         fields = '__all__'



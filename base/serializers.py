from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Magasin,Article,Response,Events
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = '__all__'

class MagasinSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Magasin
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Article
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Response
        fields = '__all__'
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Events
        fields = '__all__'
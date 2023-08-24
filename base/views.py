from django.shortcuts import render
#from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from base.models import *

# Create your views here.

def getRoutes(request):
    routes=[
        '/api/products/',
        '/api/products/create/',
        
        '/api/products/upload/',
        '/api/products/<id>/reviews/',

        '/api/products/top/'
        '/api/products/id/'

        '/api/products/delete/<id>/'
        '/api/products/<update>/<id>/'	
    ]
    return Response(routes)


@api_view(['GET'])
def getEvents(request):
    events = Events.objects.all()    
    serailizer = EventsSerializer(events, many=True)
    return Response(serailizer.data)

# class EventsListView(APIView):
#     def get(self, request, *args, **kwargs):
#         events = Events.objects.all()
#         serializer = EventsSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class EventsListView(APIView):
#     def get(self, request, *args, **kwargs):
#         events = Events.objects.all()
#         print("event",events)
#         serializer = EventsSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

    
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)

#         serializer = UserSerializerWithToken(self.user).data
#         for k, v in serializer.items():
#             data[k] = v

#         return data


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# @api_view(['POST'])
# def registerArticle(request):
#     data = request.data
#     user = request.user

#     try:
#         article = Article.objects.create(
#             user_art=user,
#             title_art=data['title_art'],
#             content_art=data['content_art'],
#             created_date_art=data['created_date_art'],
#             update_date_art=data['update_date_art'],
#         )

#         serializer = ArticleSerializerWithToken(Article, many=False)
#         return Response(serializer.data)
#     except:
#         message = {'detail': 'User with this email already exists'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def getAllArticle(request):
#     articles = Article.objects.all()    
#     serailizer = ArticleSerializer(products, many=True)
#     return Response(serailizer.data)

# @api_view(['GET'])
# def getProdcuts(request):
#     products = Product.objects.all()    
#     serailizer = ProductSerializer(products, many=True)
#     return Response(serailizer.data)

# @api_view(['GET'])
# def getMagasin(request):
#     magasin = Magasin.objects.all()    
#     serailizer = MagasinSerializer(magasin, many=True)
#     return Response(serailizer.data)

def about(request):

    return render(request, 'base/about.html')

def blogContent(request):
        
    return render(request, 'base/blog.html')

def gallery(request):


    return render(request, 'base/gallery.html')

def designer(request):

    return render(request, 'base/designer.html')


def photographe(request):

    return render(request, 'base/photographe.html')

def developper(request):

    return render(request, 'base/developper.html')

def team(request):

    return render(request, 'base/team.html')

def details(request, id):

    return render(request, 'base/detailBlog.html')
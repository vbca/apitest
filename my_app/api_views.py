from . import models, serializers
from rest_framework import viewsets, views, status, filters, pagination, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token


'''class PersonView(views.APIView):
     Regresa una lista de personas. Metodos permitidos: GET
     def get(self, request, format = None):
         serial = serializers.PersonSerializer(models.Person.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         serial = serializers.PersonSerializer(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response(serial.data, status=status.HTTP_201_CREATED)
         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)'''


'''class PersonView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    # permission_classes = [TokenHasScope]
    # required_scopes = ['read']
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name',)
    ordering_fields=('name',)'''

# class PersonView(generics.ListAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer

# class PersonView(generics.ListAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name','program__name')

#class PersonView(views.APIView):

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    # def get(self, request, format=None):
    #     user = request.user
    #     print(request.user)

    #     return Response({"hola":{"mundo"}})


# class PersonViewset(viewsets.ModelViewSet):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer

class PersonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

# class FileUploadView(views.APIView):
    
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename, format=None):
#         file_obj = request.FILES['file']
#         f = open('/tmp/test_upload', 'w')
#         f.write('test123\n')
#         f.close()
#         f = open('/tmp/test_upload', 'rb')
#         return Response(status=204)

class CompanyView(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.CompanySerializer(models.Company.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         serial = serializers.CompanySerializer(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response(serial.data, status=status.HTTP_201_CREATED)
         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

from django.core import serializers

class CompanyCreate(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.CompanySerializer(models.Company.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         username= request.POST.get("user", "")
         user = User.objects.get(username__iexact=username)
         data = serializers.serialize('json', user)
         return Response(user, status=status.HTTP_201_CREATED)
         #return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class Complaint_Category(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.Complaint_Category(models.Complaint_Category.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         serial = serializers.Complaint_Category(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response(serial.data, status=status.HTTP_201_CREATED)
         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)        

class Complaint(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.Complaint(models.Complaint.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         serial = serializers.Complaint(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response(serial.data, status=status.HTTP_201_CREATED)
         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)    


class Article(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.Article(models.Article.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         serial = serializers.Article(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response(serial.data, status=status.HTTP_201_CREATED)
         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST) 

from django.contrib.auth import authenticate, login

class Login(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.Article(models.Article.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):        
         user= request.POST.get("user", "")
         passw= request.POST.get("pass", "")
         user = authenticate(request, username=user, password=passw)
         if user is not None:
             return JsonResponse({'message':"Login Success"}, status=200)
         else:
             return JsonResponse({'message':"Check user and password"}, status=400)

class Register(views.APIView):
     '''Regresa una lista de personas. Metodos permitidos: GET'''
     def get(self, request, format = None):
         serial = serializers.Article(models.Article.objects.all(), many=True)
         return Response(serial.data)

     def post(self, request, format=None):
         username= request.POST.get("user", "")
         usermail= request.POST.get("email", "")
         password= request.POST.get("pass", "")    

         user = User.objects.create_user(username, usermail, password)
         user.save()

         current_site = get_current_site(request)
         subject = 'Activate Your MySite Account'
         message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
         })
         email=requests.post("https://api.mailgun.net/v3/sandboxad9cd8e4a5b6406bbad9ecf8df33e478.mailgun.org/messages",
         auth=("api", "key-7124e970a7e008364adcf4547e029678"),
         data={"from": "Mailgun Sandbox <postmaster@sandboxad9cd8e4a5b6406bbad9ecf8df33e478.mailgun.org>",
              "to": "Victor Garcia <vic-bailon@outlook.com>",
              "subject": subject,
              "text": message})
         print (email)
         return JsonResponse({'message':"Login Success"}, status=200)
        
             
         
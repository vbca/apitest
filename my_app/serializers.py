from rest_framework import serializers
from . import models, validators

class Contact(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ContactSerializer(serializers.Serializer):
    name  = serializers.CharField(max_length = 240)
    email = serializers.EmailField(max_length = 240)
    age = serializers.IntegerField(required=False, validators=[validators.age_validation])

    def validate_name(self, value):
        if value not in value.lower():
            raise serializers.ValidationError("necesitamos minusculas")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ('id', 'name')

class PersonSerializer(serializers.ModelSerializer):

    # program = ProgramSerializer(read_only=True)

    class Meta:
        model = models.Person
        fields = '__all__'
        # depth = 1


#####################################################        
class CompanySerializer(serializers.ModelSerializer): 
    # program = ProgramSerializer(read_only=True)
    class Meta:
        model = models.Company
        fields = '__all__'
        # depth = 1

class Complaint_Category(serializers.ModelSerializer): 
    # program = ProgramSerializer(read_only=True)
    class Meta:
        model = models.Complaint_Category
        fields = '__all__'
        # depth = 1      

class Complaint  (serializers.ModelSerializer): 
    # program = ProgramSerializer(read_only=True)
    class Meta:
        model = models.Complaint  
        fields = '__all__'
        # depth = 1   

class Article  (serializers.ModelSerializer): 
    # program = ProgramSerializer(read_only=True)
    class Meta:
        model = models.Article  
        fields = '__all__'
        # depth = 1   
        
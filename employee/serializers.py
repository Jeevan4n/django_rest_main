from rest_framework import serializers
from . import models
from models import employe

class employeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employe
        fields='__all__' 



from rest_framework import serializers
from .models import *

class CryptoCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model=CryptoCoin
        fields='__all__'

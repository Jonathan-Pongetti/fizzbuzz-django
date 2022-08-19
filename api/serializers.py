from rest_framework.serializers import ModelSerializer
from .models import FizzBuzz

class FizzBuzzSerializer(ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = '__all__'
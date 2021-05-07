from rest_framework import  serializers
from .models import Friends
class Friendserializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'
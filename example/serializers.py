from rest_framework import serializers

from example.models import Like, Dislike

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Like
       fields = '__all__'


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Dislike
       fields = '__all__'
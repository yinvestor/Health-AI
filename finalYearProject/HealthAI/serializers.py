from rest_framework import serializers
from .models import CheckUp

class CheckUpAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckUp
        exclude = ['patient']  # API doesn't require linking to patient model
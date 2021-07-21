
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Rubric


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = "__all__"
        read_only_fields = ["total_score", "percent"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class ProctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

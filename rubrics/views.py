from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from .models import Rubric
from .permissions import IsStudentOrReadOnly
from .serializers import RubricSerializer, StudentSerializer, ProctorSerializer
from django.contrib.auth import get_user_model


class RubricList(ListCreateAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class RubricDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStudentOrReadOnly,)
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer

class StudentList(ListAPIView):
    queryset = get_user_model().objects.filter(is_staff=False)
    serializer_class = StudentSerializer

class ProctorList(ListAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = ProctorSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Rubric
from .permissions import IsOwnerOrReadOnly
from .serializers import RubricSerializer


class RubricList(ListCreateAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class RubricDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer

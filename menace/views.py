from rest_framework import generics

# Create your views here.
from menace.serializers import PersonSerializer, FactSerializer, FactTitleSerializer


class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonSerializer


class FactCreateView(generics.CreateAPIView):
    serializer_class = FactSerializer


class FactTitleCreateView(generics.CreateAPIView):
    serializer_class = FactTitleSerializer

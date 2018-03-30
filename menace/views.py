from rest_framework import generics

# Create your views here.
from menace.serializers import PersonSerializer


class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonSerializer

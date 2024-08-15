from .models import Person
from .serializers import PersonSerializer

# USING APPROACH 1

# from rest_framework import generics
# class PersonListView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonDetailView(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonUpdateView(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonDeleteView(generics.DestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonCreateView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# ----------------------------------------------

# USING APPROACH 2

from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
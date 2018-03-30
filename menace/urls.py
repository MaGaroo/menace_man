from django.urls import path

from . import views

urlpatterns = [
    path(r'person/create/', views.PersonCreateView.as_view(), name='person_create'),
]

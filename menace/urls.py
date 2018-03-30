from django.urls import path

from . import views

urlpatterns = [
    path(r'person/create/', views.PersonCreateView.as_view(), name='person_create'),
    path(r'fact/create/', views.FactCreateView.as_view(), name='fact_create'),
    path(r'fact_title/create/', views.FactTitleCreateView.as_view(), name='fact_title_create'),
]

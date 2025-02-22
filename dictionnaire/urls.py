from django.urls import path
from .views import *

urlpatterns = [ 
    path('eton', MotEtonView.as_view(), name='mots'),
    path('eton/recherche', RechercheMotFrancaisView.as_view(), name='recherche-francais')
]
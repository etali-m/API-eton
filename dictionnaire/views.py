from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import classeGrammaticale, MotEton, Traduction
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MotEtonView(GenericAPIView):
    queryset = MotEton.objects.all()
    serializer_class = MotEtonSerializer

    def get(self, request):
        mot = self.request.GET.get('mot')

        queryset = self.get_queryset()  # Récupérer le queryset défini dans la classe

        if mot:
            queryset = queryset.filter(mot_eton__icontains=mot)  # Filtrer sur le champ "mot_eton"

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RechercheMotFrancaisView(APIView):
    def get(self, request):
        mot_francais = request.GET.get('mot')
        if mot_francais:
            traductions = Traduction.objects.filter(mot_francais__icontains=mot_francais)
            mots_eton = MotEton.objects.filter(traductions__in=traductions).distinct()
            serializer = MotEtonSerializer(mots_eton, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Le paramètre 'mot' est requis."}, status=status.HTTP_400_BAD_REQUEST)
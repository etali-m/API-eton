from rest_framework import serializers 
from .models import *

class ClasseGrammaticaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = classeGrammaticale
        fields = ['id', 'abbreviation', 'nom', 'description']

class ClassNominaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseNominale
        fields = ['id', 'nom', 'description']


class ExempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemple
        fields = ['id', 'phrase_eton', 'phrase_francais', 'prononciation']


class TraductionSerializer(serializers.ModelSerializer):
    exemples = ExempleSerializer(many=True, read_only=True)

    class Meta:
        model = Traduction
        fields = ['id', 'mot_francais', 'definition', 'image', 'exemples']


class SimpleMotEtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotEton
        fields = ['id', 'mot_eton', 'pluriel', 'sens_litteral', 'prononciation']

class MotEtonSerializer(serializers.ModelSerializer):
    class_grammaticale = ClasseGrammaticaleSerializer()
    classe_nominale = ClassNominaleSerializer()
    mot_reference = serializers.SerializerMethodField()
    synonyme = serializers.SerializerMethodField()
    traductions = serializers.SerializerMethodField()

    class Meta:
        model = MotEton
        fields = ['id', 'mot_eton', 'pluriel', 'class_grammaticale', 'sens_litteral', 'classe_nominale', 'mot_reference', 'synonyme', 'prononciation', 'traductions']

    def get_mot_reference(self, obj):
        return SimpleMotEtonSerializer(obj.mot_reference.all(), many=True).data

    def get_synonyme(self, obj):
        return SimpleMotEtonSerializer(obj.synonyme.all(), many=True).data

    def get_traductions(self, instance):
        query_set = instance.traductions.all()
        serializer = TraductionSerializer(query_set, many=True)
        return serializer.data
    
class SearchFrancaisSerializer(serializers.ModelSerializer):
    traductions = TraductionSerializer(many=True, read_only=True)

    class Meta:
        model = MotEton
        fields = ['mot_eton', 'pluriel','prononciation', 'traductions']    
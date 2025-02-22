from rest_framework import serializers 
from .models import *

class ClasseGrammaticaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = classeGrammaticale
        fields = ['id', 'abbreviation', 'nom', 'description']

class TraductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traduction
        fields = ['id', 'mot_francais', 'description', 'image', 'phrase_eton', 'phrase_francais', 'prononciation']


class SimpleMotEtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotEton
        fields = ['id', 'mot_eton', 'pluriel', 'prononciation']

class MotEtonSerializer(serializers.ModelSerializer):
    class_grammaticale = ClasseGrammaticaleSerializer(many=True)
    mot_reference = serializers.SerializerMethodField()
    synonyme = serializers.SerializerMethodField()
    traductions = serializers.SerializerMethodField()

    class Meta:
        model = MotEton
        fields = ['id', 'mot_eton', 'pluriel', 'class_grammaticale', 'mot_reference', 'synonyme', 'prononciation', 'traductions']

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
from pyexpat import model
from rest_framework import serializers
from app import models

class CadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cad_Mapeamento
        fields = '__all__'
class CadSetoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cad_setores
        fields = '__all__'
class CadEquipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cad_equipes
        fields = '__all__'
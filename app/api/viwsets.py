from rest_framework import viewsets
from app.api import serializers
from app import models

class CadMapViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadMapSerializer
    queryset = models.Cad_Mapeamento.objects.all()
class CadSetoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadSetoresSerializer
    queryset = models.Cad_setores.objects.all()
class CadEquipesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadEquipesSerializer
    queryset = models.Cad_equipes.objects.all()

class ItensAuditaveisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItensAuditaveisSerializer
    queryset = models.Cad_itens_auditaveis.objects.all()
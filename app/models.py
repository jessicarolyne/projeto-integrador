# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
#from django.contrib.auth.models import User


class Cad_empresa(models.Model):
    nome_fantasia_empresa = models.CharField(max_length=80)
    cnpj_empresa = models.CharField(max_length=18)
    endereco_empresa = models.CharField(max_length=80)
    cidade_empresa = models.CharField(max_length=80)
    cep_empresa = models.CharField(max_length=9)
    estado_empresa = models.CharField(max_length=40)
    telefone_empresa = models.CharField(max_length=15)

from django.db.models import Count
class Cad_setores(models.Model):
    setor_nome = models.CharField(max_length=30)
    resposavel_setor = models.CharField(max_length=30)
    cargo_setor = models.CharField(max_length=30)
    contato_setor = models.CharField(max_length=30)


class Cad_equipes(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    responsabilidade = models.CharField(max_length=30)

class Cad_fornecedores(models.Model):
    fornecedor = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)
    dpo = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

class Cad_dpo(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    contato = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)

class Cad_dados_previos(models.Model):
    questao_dados_previos = models.CharField(max_length=90)
    resposta = models.CharField(max_length=10)

class Cad_itens_auditaveis(models.Model):
    questao_itens_auditaveis = models.CharField(max_length=90)
    il = models.IntegerField()
    icn = models.IntegerField()
    e = models.IntegerField()
    fr = models.IntegerField()

    @property
    def fr(self):
        return (self.il ** 2 + self.icn ** 2)*((7-self.e) ** 2) 

    
class Cad_fator_de_risco(models.Model):
    questao_fator_de_risco = models.CharField(max_length=90)
    fator_de_risco = models.IntegerField()
    #fator_de_risco = Cad_itens_auditaveis.fr()
    ##CALCULO DO FATOR DE RISCO fr = (il ** 2 + icn ** 2)*((7-e) ** 2) 

class Cad_Mapeamento(models.Model):
    dado = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    fonte = models.CharField(max_length=30)
    motivo = models.CharField(max_length=30)
    base_legal = models.CharField(max_length=30)
    tratamento = models.CharField(max_length=30)
    eliminacao = models.CharField(max_length=30)
    compartilhamento = models.CharField(max_length=30)
    necessario_consentimento = models.CharField(max_length=30)
    possui_consentimento = models.CharField(max_length=30)
    menor = models.CharField(max_length=30)
    impacto_pessoal = models.CharField(max_length=30)
    missao_critica = models.CharField(max_length=30)
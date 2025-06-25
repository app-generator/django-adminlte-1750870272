# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Veiculos(models.Model):

    #__Veiculos_FIELDS__
    nomeveiculo = models.CharField(max_length=255, null=True, blank=True)
    placa = models.CharField(max_length=255, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    chassis = models.CharField(max_length=255, null=True, blank=True)
    cor = models.CharField(max_length=255, null=True, blank=True)
    clienteproprietariocrv = models.CharField(max_length=255, null=True, blank=True)
    rntrc = models.CharField(max_length=255, null=True, blank=True)
    proprietarioantt = models.CharField(max_length=255, null=True, blank=True)
    capacidadepassageiro = models.IntegerField(null=True, blank=True)
    tarakg = models.CharField(max_length=255, null=True, blank=True)
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE)
    inativo = models.BooleanField()
    codigosistema = models.IntegerField(null=True, blank=True)

    #__Veiculos_FIELDS__END

    class Meta:
        verbose_name        = _("Veiculos")
        verbose_name_plural = _("Veiculos")


class Combustivel(models.Model):

    #__Combustivel_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Combustivel_FIELDS__END

    class Meta:
        verbose_name        = _("Combustivel")
        verbose_name_plural = _("Combustivel")


class Contratos(models.Model):

    #__Contratos_FIELDS__
    emissaocontrato = models.DateTimeField(blank=True, null=True, default=timezone.now)
    vencimentocontrato = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nomecliente = models.CharField(max_length=255, null=True, blank=True)
    tipocontrato = models.CharField(max_length=255, null=True, blank=True)
    valor = models.CharField(max_length=255, null=True, blank=True)
    objetocontrato = models.CharField(max_length=255, null=True, blank=True)
    obs = models.TextField(max_length=255, null=True, blank=True)
    formapag = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)

    #__Contratos_FIELDS__END

    class Meta:
        verbose_name        = _("Contratos")
        verbose_name_plural = _("Contratos")


class Formapagamento(models.Model):

    #__Formapagamento_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Formapagamento_FIELDS__END

    class Meta:
        verbose_name        = _("Formapagamento")
        verbose_name_plural = _("Formapagamento")



#__MODELS__END

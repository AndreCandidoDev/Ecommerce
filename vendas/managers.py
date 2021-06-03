from django.db import models
from django.db.models import Max, Avg, Min, Count

# usar managers em metodos que iteragem com o BD inteiro
# se a função usar apenas uma query usar função no model


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(
            Avg('valor'))['valor__avg']

    def media_desc(self):
        return self.all().aggregate(
            Avg('desconto'))['desconto__avg']

    def min(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def max(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def cont(self):
        return self.all().aggregate(Count('id'))['id__count']

    def cont_nfes(self):
        return self.filter(nfe_emitida=True).aggregate(
            Count('id'))['id__count']
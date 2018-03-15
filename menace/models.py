from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name=_('First Name'),
                                  max_length=100,
                                  blank=False,
                                  null=False)
    last_name = models.CharField(verbose_name=_('Last Name'),
                                 max_length=100,
                                 blank=False,
                                 null=False)


class Fact(models.Model):
    body = models.TextField(verbose_name=_('Fact'),
                            null=False,
                            blank=False)
    person = models.ForeignKey(Person,
                               verbose_name=_('Person'),
                               on_delete=models.CASCADE,
                               null=False)

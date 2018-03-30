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

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.pk)


class FactTitle(models.Model):
    name = models.CharField(verbose_name=_('Fact Title'),
                            max_length=100,
                            blank=False,
                            null=False)

    def __str__(self):
        return self.name


class Fact(models.Model):
    title = models.ForeignKey(FactTitle,
                              verbose_name=_('Title'),
                              on_delete=models.SET_NULL,
                              null=True)
    body = models.TextField(verbose_name=_('Fact'),
                            null=False,
                            blank=False)
    person = models.ForeignKey(Person,
                               verbose_name=_('Person'),
                               on_delete=models.CASCADE,
                               null=False)

    def __str__(self):
        return '{}{}'.format(self.body[:20], (' ...' if len(str(self.body)) > 20 else ''))

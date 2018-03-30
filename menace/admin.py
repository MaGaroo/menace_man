from django.contrib import admin

# Register your models here.
from menace.models import Person, Fact

admin.site.register(Person)
admin.site.register(Fact)

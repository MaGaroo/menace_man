from rest_framework import serializers

from menace.models import Person, Fact, FactTitle


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'


class FactTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactTitle
        fields = '__all__'

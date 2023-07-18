from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


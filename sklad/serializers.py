from .models import Trotuarka, Zabor, Materials, Sklad, Izdelie
from rest_framework import serializers


# class SkladSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Sklad
#         fields = ('storage',)


class TroruarkaSerializer(serializers.ModelSerializer):
    # sklad = SkladSerializer()

    class Meta:
        model = Trotuarka
        fields = ('name', 'color', 'description', 'price', 'amount', 'id', 'price', 'getsklad')



class ZaborSerializer(serializers.ModelSerializer):
    # sklad = SkladSerializer()

    class Meta:
        model = Zabor
        fields = ('name', 'description', 'price', 'amount', 'id', 'getsklad')
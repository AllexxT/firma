from .models import Trotuarka, Zabor, Materials, Sklad, Izdelie, ColorAndPrice
from rest_framework import serializers


class SkladSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sklad
        fields = (
            'storage',
        )

class ColorAndPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorAndPrice
        fields = (
            'color',
            'cost',
            'amount',
            # 'show'
        )


class TroruarkaSerializer(serializers.ModelSerializer):
    getinfo = ColorAndPriceSerializer(read_only=True, many=True)

    class Meta:
        model = Trotuarka
        fields = (
            'name',
            'description',
            'id',
            'getsklad',
            'getinfo'
        )



class ZaborSerializer(serializers.ModelSerializer):
    # getsklad = SkladSerializer()

    class Meta:
        model = Zabor
        fields = (
            'name', 
            'description', 
            'price', 
            'amount', 
            'id', 
            'getsklad'
        )


class ZaborPostSerializer(serializers.ModelSerializer):
    # sklad = SkladSerializer()

    class Meta:
        model = Zabor
        fields = (
            'name', 
            'description', 
            'price', 
            'amount', 
            'sklad',
        )
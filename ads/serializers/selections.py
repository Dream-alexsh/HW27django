from rest_framework import serializers

from ads.models import Selection, Ad
from ads.serializers.ads import AdSerializer


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='id')
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
   class Meta:
        model = Selection
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'



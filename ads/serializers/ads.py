from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    # category = serializers.SlugRelatedField(read_only=True,
    #                                         slug_field='name')

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

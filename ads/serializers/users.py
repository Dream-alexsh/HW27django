import datetime
from rest_framework import serializers
from ads.models import User, Location


def date_is_not_nine_years(value):
    year = datetime.date.today() - value
    year = int(year.total_seconds()/(3600*24*365))

    if year < 9:
        raise serializers.ValidationError(f'You must be over 9 years old to register')


def email_not_rambler(value):
    domain = value.split('@')[-1]

    if domain == 'rambler.ru':
        raise serializers.ValidationError(f'Just not rambler, pls')


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, read_only=True,
                                             slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, queryset=Location.objects.all(), slug_field='name')
    birth_date = serializers.DateField(required=False, validators=[date_is_not_nine_years])
    email = serializers.EmailField(required=False, validators=[email_not_rambler])

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for locations in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(location_obj)

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, queryset=Location.objects.all(), slug_field='name')

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for locations in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(location_obj)

        user.save()
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

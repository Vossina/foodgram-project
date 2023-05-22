
import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
import webcolors

from .models import Tag, Ingredient, Recipe
from users.serializers import UserSerializer

class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value
    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(
        slug_field='name', queryset=Tag.objects.all())
    color = Hex2NameColor()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'color')


class IngredientSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=250)
    # measurement_unit = serializers.CharField(max_length=10)

    class Meta:
        model = Ingredient
        fields = ('id', 'amount', 'name', 'measurement_unit')

class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    ingredients = IngredientSerializer(many=True)
    image = Base64ImageField(allow_null=True, required=False)

    class Meta:
        model = Recipe
        fields = '__all__'
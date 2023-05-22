from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    measurement_unit = models.CharField(max_length=10)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.amount}, {self.name}, {self.measurement_unit}'

class Recipe(models.Model):
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, related_name='ingredients', on_delete=models.CASCADE)
    is_favorited = models.BooleanField()
    is_in_shoping_cart = models.BooleanField()
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, default=None, upload_to='recipes/image/')
    text = models.TextField()
    cooking_time = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.author}, {self.name}'
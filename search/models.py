"""Models of the Pur Beurre website - Data from the OpenFoodFacts API
Initialized by the init_db.py file
"""
from django.db import models
from django.contrib.auth.models import User


class categorie(models.Model):
    """Store some categories of product"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class op_food(models.Model):
    """Stores openfoodfact API products"""
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    ingredient = models.CharField(max_length=2000)
    nutritional_values = models.CharField(max_length=100)
    url = models.URLField()
    picture = models.URLField(null=True)
    picture_100g = models.URLField(null=True)
    categorie = models.ForeignKey(categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class substitute(models.Model):
    """Stores favorite products with product ID and user ID"""
    id_substitute = models.ForeignKey(op_food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.id, self.id_substitute.id

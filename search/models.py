"""Models of the Pur Beurre website - Data from the OpenFoodFacts API
Initialized by the init_db.py file
"""
from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    """Store some categories of product"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
	"""Stores the list of store names and coordinates"""
	name_store = models.CharField(max_length=100)
	coordinates = models.FloatField()

	def __str__(self):
		return self.name_store

class Op_food(models.Model):
    """Stores openfoodfact API products"""
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    ingredient = models.CharField(max_length=2000)
    nutritional_values = models.CharField(max_length=100)
    url = models.URLField()
    picture = models.URLField(null=True)
    picture_100g = models.URLField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    store_available = models.ManyToManyField(Store)

    def __str__(self):
        return self.name


class Substitute(models.Model):
    """Stores favorite products with product ID and user ID"""
    id_substitute = models.ForeignKey(Op_food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.id, self.id_substitute.id


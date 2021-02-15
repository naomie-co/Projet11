"""Script to initialize the platform database from the OpenFoodFacts API"""

import requests
from django.core.management.base import BaseCommand
from search.models import categorie, op_food, substitute
from search.const import CATEGORIES



class Command(BaseCommand):
    """This class aims to interact with the OpenfoodFact's API
    Its parameters aims to prepared the request
    Its request_product method made the resquest
    """
    def __init__(self):
        """Parameters for the API request"""
        self.url = 'https://world.openfoodfacts.org/cgi/search.pl'
        self.param = {
            'action':'process',
            'tagtype_0':'categories',
            'tag_contains_0':'contains',
            'tag_0':'',
            'page_size':50,
            'json':1
        }

    def categorie_db(self):
        """Insert categories into .models categorie's table"""
        for elt in CATEGORIES:
            cat = categorie()
            cat.name = elt
            #cat.clean()
            cat.save()
        return cat

    def request_product(self, tag):
        """Get products from the API depending on the tag in parameter.
        Store the result in a list of list named data
        Return data """
        i = 0
        self.param["tag_0"] = tag
        request = requests.get(self.url, params=self.param)
        result = request.json()
        data = []
        for val in result["products"]:
            try:
                data.append([val["product_name_fr"],\
                val["nutrition_grades"], val["ingredients_text_fr"],\
                val["image_nutrition_url"], val["image_url"], val["url"]])
                i += 1
                if i > 40:
                    break
            except KeyError:
                print("Erreur dans la réception des données : ", val)
        return data

    def search_product(self):
        """From the categories of the category table, launch a request to the
        OFF API with the request_product method. Retrieve the OFF data to
        insert into the op_food table"""
        categories = categorie()
        categories = categorie.objects.all()
        for cat in categories:
            for value in self.request_product(cat.name):
                new_values = op_food(categorie=cat, \
                name=value[0], nutriscore=value[1], ingredient=value[2], \
                picture_100g=value[3], picture=value[4], url=value[5])
                new_values.save()

    def delete_data(self):
        """Delete data from categorie, op_food and substitute tables"""
        categorie.objects.all().delete()
        op_food.objects.all().delete()
        substitute.objects.all().delete()

    def handle(self, *args, **options):
        """Delete data then fill the database
        """
        self.delete_data()
        self.categorie_db()
        self.search_product()

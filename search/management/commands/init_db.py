"""Script to initialize the platform database from the OpenFoodFacts API"""

import requests
from django.core.management.base import BaseCommand
from search.models import Categorie, Op_food, Substitute, Store
from search.const import CATEGORIES
import csv




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
            'page_size':10,
            'json':1
        }

    def categorie_db(self):
        """Insert categories into .models Categorie's table"""
        for elt in CATEGORIES:
            cat = Categorie()
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
                val["image_nutrition_url"], val["image_url"], val["url"], val["stores"]])
                i += 1
                if i > 5:
                    break
            except KeyError:
                print("Erreur dans la réception des données : ", val)
        return data

    def convert_string(self, string):
        string = string.lower()
        new_list = list(string.split(","))
        return new_list

    def search_product(self):
        """From the categories of the Category table, launch a request to the
        OFF API with the request_product method. Retrieve the OFF data to
        insert into the Op_food table"""
        categories = Categorie()
        categories = Categorie.objects.all()
        for cat in categories:
            for value in self.request_product(cat.name):
                list_of_stores = self.convert_string(value[6])
                print(list_of_stores)
                new_product = Op_food.objects.create(categorie=cat, \
                name=value[0], nutriscore=value[1], ingredient=value[2], \
                picture_100g=value[3], picture=value[4], url=value[5])
                search_store = Store.objects.filter(name_store=list_of_stores[0])
                #print(search_store)
                for elt in search_store: 
                    new_product.store_available.add(elt)


                #print(type(list_of_stores), value[0], list_of_stores)
                        

                #test to check if a product is inserted only once in the table
                # test = Op_food.objects.filter(name=value[0])
                # print(test)


    def add_store(self):
        """
        Add store in the Store's table from a csv file
        """
        with open("stores_locations.csv", encoding="utf-8") as stores:
            reader = csv.reader(stores)
            next(reader, None)

            for row in reader:
                Store.objects.create(
                name_store=row[0],
                latitude=row[1],
                longitude=row[2],)
     



    def delete_data(self):
        """Delete data from Categorie, Op_food and Substitute tables"""
        #Store.objects.all().delete()
        Categorie.objects.all().delete()
        Op_food.objects.all().delete()
        Substitute.objects.all().delete()

    def handle(self, *args, **options):
        """Delete data then fill the database
        """
        #if categorie.objects.count() == 0: 
        #    self.categorie_db()
        #    self.search_product()
        #else:
        #    self.search_product()


        self.delete_data()
        #self.add_store()
        self.categorie_db()
        self.search_product()

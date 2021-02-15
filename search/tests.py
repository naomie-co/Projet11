
"""Tests views and the database models"""

from django.urls import reverse
from django.test import TestCase 
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from search.models import categorie, op_food


class IndexPageTestCase(TestCase):
    """test that index page returns a status code 200"""
    def test_index_page(self):
        """index_page status code test"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class LegalTestCase(TestCase):
    """test that legal page returns a status code 200"""
    def test_legal_page(self):
        """Legal page status code test"""
        response = self.client.get(reverse('search:legal'))
        self.assertEqual(response.status_code, 200)


class ProductsPagesTestCase(TestCase):
    """Tests products page and selection page"""

    def setUp(self):
        """Setup products in the models"""
        test_categorie = categorie.objects.create(name="Taboulé")
        self.cat = categorie.objects.get(name="Taboulé")
        test_product1 = op_food.objects.create(name="Taboulé", \
        nutriscore="d", ingredient="test", nutritional_values="test", \
        url="www.test.fr", picture="", picture_100g="", categorie=self.cat)
        test_product2 = op_food.objects.create(name="Taboulé2", \
        nutriscore="c", ingredient="test2", nutritional_values="test2", \
        url="www.test2.fr", picture="", picture_100g="", categorie=self.cat)
        self.product1 = op_food.objects.get(name="Taboulé")
        self.product2 = op_food.objects.get(name="Taboulé2")
        self.user = User.objects.create(username="test_1", is_active=1)
        self.user.set_password("password")
        self.user.save()

    def test_detail_page_returns_200(self):
        """test that detail page returns a status code 200"""
        product_id = self.product1.id
        reponse = self.client.get(reverse('search:detail', args=(product_id,)))
        self.assertEqual(reponse.status_code, 200)

    def test_detail_page_returns_404(self):
        """test that detail page returns a status code 404 if the items does
        not exist"""
        product_id = self.product1.id + 2
        reponse = self.client.get(reverse('search:detail', args=(product_id,)))
        self.assertEqual(reponse.status_code, 404)

    def test_my_selection_authentificated(self):
        """Test that my_selection page returns a status code 303 to log_in page
        if the user is not authentificated"""
        user_test = {"user":234}
        reponse = self.client.get(reverse('search:my_selection', \
        args=(user_test)))
        self.assertEqual(reponse.status_code, 302)

    def test_products_page(self):
        """Test that if the user logs in, the product page is different from the u
        unconnected version"""

        page_without_log = self.client.get(reverse('search:products'))
        self.client.force_login(user=self.user)
        reponse = self.client.get(reverse('search:products'))
        self.assertIn(b'<i class="fas fa-sign-out-alt fa-2x"', 
            reponse.content)
        self.assertNotIn(b'<i class="fas fa-sign-out-alt fa-2x"', page_without_log.content)

class DataBaseTestCase(TestCase):
    """Test database models"""

    def setUp(self):
        """setup products in the models"""
        test_categorie = categorie.objects.create(name="Taboulé")
        self.cat = categorie.objects.get(name="Taboulé")
        test_product1 = op_food.objects.create(name="Taboulé", \
        nutriscore="d", ingredient="test", nutritional_values="test", \
        url="www.test.fr", picture="", picture_100g="", categorie=self.cat)
        test_product2 = op_food.objects.create(name="Taboulé2", \
        nutriscore="c", ingredient="test2", nutritional_values="test2", \
        url="www.test2.fr", picture="", picture_100g="", categorie=self.cat)
        self.product1 = op_food.objects.get(name="Taboulé")
        self.product2 = op_food.objects.get(name="Taboulé2")

    def test_user_create(self):
        """Test that a new user is created"""
        User.objects.create_user('user_test', 'user_test@test.com', \
        'testpassword')
        assert User.objects.count() == 1

    def test_op_food_table(self):
        """Test that a new obejct is created"""
        old_products = op_food.objects.count()
        op_food.objects.create(name="taboulé", nutriscore="d",\
        ingredient="test", nutritional_values="test", url="www.test.fr", \
        picture="", picture_100g="", categorie=self.cat)
        new_products = op_food.objects.count()
        self.assertEqual(new_products, old_products + 1)

    def test_categorie_table(self):
        """Test that a new categorie is created"""
        old_categorie = categorie.objects.count()
        categorie.objects.create(name="houmous")
        new_categorie = categorie.objects.count()
        self.assertEqual(new_categorie, old_categorie + 1)


# class SearchText(StaticLiveServerTestCase):
#     """Functional tests"""


#     def setUp(self):
#         """setup products in the models"""
#         test_categorie = categorie.objects.create(name="Taboulé")
#         self.cat = categorie.objects.get(name="Taboulé")
#         test_product1 = op_food.objects.create(name="Taboulé", \
#         nutriscore="d", ingredient="test", nutritional_values="test", \
#         url="www.test.fr", picture="", picture_100g="", categorie=self.cat)
#         test_product2 = op_food.objects.create(name="Taboulé2", \
#         nutriscore="c", ingredient="test2", nutritional_values="test2", \
#         url="www.test2.fr", picture="", picture_100g="", categorie=self.cat)
#         self.product1 = op_food.objects.get(name="Taboulé")
#         self.product2 = op_food.objects.get(name="Taboulé2")

#         #Create a User
#         self.user = User.objects.create(username="test_1", is_active=1)
#         self.user.set_password("password")
#         self.user.save()

#         # create a new Firefox session
#         self.driver = webdriver.Firefox(
#         executable_path=r'C:\\Program Files\\geckodriver\\geckodriver.exe')
#         self.driver.implicitly_wait(30)
#         self.driver.maximize_window()
#         # navigate to the application home page
#         self.driver.get('%s' % (self.live_server_url))

#     def test_search_user_not_log(self):
#         """Test that if a the user is not logged, the result is display with a
#         log_in button"""

#         timeout = 2
#         # get the search textbox
#         self.search_field = WebDriverWait(self.driver, timeout).until(
#             lambda driver: self.driver.find_element_by_name("query"))


#         # enter search keyword and submit
#         self.search_field.send_keys("taboulé")
#         self.search_field.submit()

#         #get the list of elements which are displayed after the search on
#         #result page elements_by_name

#         lists = WebDriverWait(self.driver, timeout).until(
#             lambda driver: self.driver.find_element_by_name("log_in"))
#         result = op_food.objects.count()
#         self.assertEqual(2, result)


#     def tearDown(self):
#         # close the browser window
#         self.driver.quit()

#     def test_search_user_log(self):
#         """Test if a user is logged in, the search page displays a backup
#         button"""

#         timeout = 2
#         # get the search textbox required to login
#         self.driver.find_element_by_name("user_i").click()
#         self.driver.find_element_by_name("username").send_keys("test_1")
#         self.driver.find_element_by_name('password').send_keys("password")
#         self.driver.find_element_by_name("log_in").click()

#         # get the search textbox
#         self.search_field = WebDriverWait(self.driver, timeout).until(
#             lambda driver: self.driver.find_element_by_name("query"))


#         # enter search keyword and submit
#         self.search_field.send_keys("taboulé")
#         self.search_field.submit()
#         #get the list of elements which are displayed after the search
#         #currently on result page usingfind_elements_by_name_namemethod

#         lists = WebDriverWait(self.driver, timeout).until(
#             lambda driver: self.driver.find_element_by_name("save"))
#         result = op_food.objects.count()
#         self.assertEqual(2, result)



    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()
from django.test import TestCase
from search.models import categorie, op_food

"""
WORK IN PROGRESS

Test the database initialization script
"""


class InitDatabaseTestCase(TestCase):
    """test the API request and the filling of the database"""
    
    @mock.patch('app.utils.requests.get')
    def test_request_product(self, mock_get): 
    	"""Mock an API request with a tag in parameter.
        Store the result in a list of list named data"""
        @mock.patch('requests.get')
        def test_request_product(self, mock_get):
        	#define new Mock object
        	mock_response = mock.Mock()
        	#define response data from OFF API
        	expected_dict = {

        	}

        	#define response data from my Mock object
        	mock_response.json.return_value = expected_dict
        	mock_response.status_code = 200

        	#define response for the fake API
        	mock_get.return_value = mock_response

        	#call the function
        	result = test_resquest_product(self, "taboulé")

        	self.assertEqual(result, { })


        pass


    def test_search_product(self):
    	"""Mocks the category table, mocks a request to the OFF API. Tests if
    	the products have entered the op_food table"""
        pass
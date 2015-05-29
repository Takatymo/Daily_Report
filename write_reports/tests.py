from django.test import TestCase, Client
from django.core.urlresolvers import reverse


# Create your tests here.
class search_reports_tests(TestCase):
    def test_for_no_keyword(self):
        """
        If users click the search button without keyword in search field,
        an appropriate message should be displayed in the index.html.
        :return:
        """

        #response = Client().post(reverse('index'), {"keyword": ""})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No keyword is inputted.")
        self.assertQuerysetEqual(response.context['reports'], [])

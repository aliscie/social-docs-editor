from django.test import TestCase

# Create your tests here.
import json
from graphene_django.utils.testing import GraphQLTestCase


class MyFancyTestCase(GraphQLTestCase):
    def test_query_posts(self):
          True
      #   response = self.query(
      #       '''
      #       query{
      #       posts {
      #       description
      #       id
      #       addedBy{
      #           username
      #           id
      #           }
      #       }
      #       }
      #       ''',
      #   )
      #   content = json.loads(response.content)
      #   self.assertResponseNoErrors(response)

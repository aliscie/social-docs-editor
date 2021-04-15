from django.test import TestCase

# Create your tests here.
import json
from graphene_django.utils.testing import GraphQLTestCase


class MyFancyTestCase(GraphQLTestCase):
    def test_query_posts(self):
        response = self.query(
            '''
            query{
            posts {
            id
            description
            comment {
            id
            description
            }
            styles
            }
            }
            '''
        )

        # content = json.loads(response.content)
        # print({"________XXXXX": content})
        # self.assertResponseNoErrors(response)

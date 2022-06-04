from django.test import TestCase, Client
from django.urls import reverse
from ..models import Recipe


class TestRecipesView(TestCase):

    recipes_url: str
    client: Client
    test_recipe: Recipe

    def setUp(self):
        self.recipes_url = reverse("core:recipes")
        self.client = Client()
        self.test_recipe = Recipe.objects.create(
            title="Quick cake recipe", text="1) Buy a cake. The end", key="secret-test"
        )
        return super().setUp()

    def tearDown(self):
        self.test_recipe.delete()
        return super().tearDown()

    def test_list_recipes(self):
        response = self.client.get(self.recipes_url)
        response_data = response.json()

        # Checking for status code
        self.assertEqual(response.status_code, 200, "Status code should be 200")

        # Checking for type of the response
        self.assertTrue(isinstance(response_data, list), "Response object should be a list")

        # Checking for the length of the response
        self.assertGreaterEqual(len(response_data), 1, "Length of the response list should be greater or equal to 1")

        response_element = response_data[0]

        # Checking for the type of the first element of the response
        self.assertTrue(isinstance(response_element, dict))

        keys = ["id", "title", "text", "created_at", "updated_at"]

        # Checking for the amount of keys of the first element
        self.assertEqual(len(response_element.keys()), len(keys), f"The object should have {len(keys)} keys")

        # Checking if each key is in the pre defined list of keys
        response_keys = response_element.keys()
        for key in response_keys:
            self.assertTrue(key in keys, f"The key {key} is not supposed to be in the object")

        # Checking if the data matches what was informed in the setUp function
        self.assertEqual(response_element["title"], "Quick cake recipe", "The title should be 'Quick cake recipe'")
        self.assertEqual(
            response_element["text"], "1) Buy a cake. The end", "The text should be '1) Buy a cake. The end'"
        )

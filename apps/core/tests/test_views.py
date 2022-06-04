from django.test import TestCase, Client
from django.urls import reverse
from ..models import Recipe


class TestRecipesView(TestCase):

    recipes_url: str
    client: Client
    test_recipe: Recipe
    mock_data = {"title": "Bolo frito recipe", "text": "1) You might just find it in a bakery!", "key": "my-recipe"}
    response_format_data = ["id", "title", "text", "created_at", "updated_at"]

    def setUp(self):
        self.recipes_url = reverse("core:recipes")
        self.client = Client()
        self.test_recipe = Recipe.objects.create(
            title="Quick cake recipe", text="1) Buy a cake. The end", key="secret-test"
        )

    def tearDown(self):
        self.test_recipe.delete()

    def assert_dictionaries(self, data: dict):

        # Checking the type of the response's object
        self.assertTrue(isinstance(data, dict), "The response data should be in a dictionary format")

        # Checking for the amount of keys of the element
        self.assertEqual(
            len(data.keys()),
            len(self.response_format_data),
            f"The object should have {len(self.response_format_data)} keys",
        )

        # Checking if each key is in the pre defined list of keys
        for key in data.keys():
            self.assertTrue(key in self.response_format_data, f"The key '{key}' is not supposed to be in the object")

    def test_list_recipes(self):
        response = self.client.get(self.recipes_url)
        response_data = response.json()

        # Checking for status code
        self.assertEqual(response.status_code, 200, "Status code should be 200")

        # Checking for type of the response
        self.assertTrue(isinstance(response_data, list), "Response object should be a list")

        # Checking for the length of the response
        self.assertGreaterEqual(len(response_data), 1, "Length of the response list should be greater or equal to 1")

        first_element = response_data[0]

        self.assert_dictionaries(data=first_element)

        # Checking if the data matches what was informed in the setUp function
        self.assertEqual(first_element["title"], "Quick cake recipe", "The title should be 'Quick cake recipe'")
        self.assertEqual(
            first_element["text"], "1) Buy a cake. The end", "The text should be '1) Buy a cake. The end'"
        )

    def test_create_recipe(self):
        response = self.client.post(self.recipes_url, data=self.mock_data, content_type="application/json")
        response_data = response.json()

        self.assertEqual(response.status_code, 201, "Status code should be 201")

        self.assert_dictionaries(data=response_data)

        Recipe.objects.get(id=response_data["id"]).delete()

        # Checking if the values matches with what was informed in the request
        keys = ["title", "text"]
        for key in keys:
            self.assertEqual(
                response_data[key],
                self.mock_data[key],
                f"The response value for {key} should be '{self.mock_data[key]}' not {response_data[key]}",
            )

        response = self.client.post(self.recipes_url, data=dict(), content_type="application/json")
        self.assertEqual(response.status_code, 400, "Should not be able to create an empty recipe")

        response = self.client.post(
            self.recipes_url, data={"title": self.mock_data["title"]}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400, "Should not be able to create a recipe without text and key")

        response = self.client.post(
            self.recipes_url, data={"text": self.mock_data["text"]}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400, "Should not be able to create a recipe without title and key")

        response = self.client.post(
            self.recipes_url, data={"key": self.mock_data["key"]}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400, "Should not be able to create a recipe without title and text")

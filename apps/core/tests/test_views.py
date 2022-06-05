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
        """
        This method is a helper to assert that the data is in a dictionary format, has a n amount of keys and if those keys are the
        same as the pre defined keys
        """

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

    def test_create_recipe(self):
        """
        This method tests if the 'create_recipe' method of the RecipesViewSet is able to create a recipe with the given data
        """
        response = self.client.post(self.recipes_url, data=self.mock_data, content_type="application/json")
        response_data = response.json()

        self.assertEqual(response.status_code, 201, "Status code should be 201")
        self.assert_dictionaries(data=response_data)

        recipe = None
        try:
            recipe = Recipe.objects.get(id=response_data["id"])
        except:
            pass

        # The Recipe item should exists in the database with the id returned
        self.assertTrue(isinstance(recipe, Recipe), "The recipe should exists in the database")

        # Checking if the values matches with what was informed in the request
        keys = ["title", "text", "key"]
        for key in keys:
            db_value = getattr(recipe, key)
            self.assertEqual(
                db_value,
                self.mock_data[key],
                f"The value for {key} should be '{self.mock_data[key]}' not {db_value}",
            )

        # Checking if the view doesn't allow the creation of empty recipes
        response = self.client.post(self.recipes_url, data=dict(), content_type="application/json")
        self.assertEqual(response.status_code, 400, "Should not be able to create an empty recipe")

        # Checking if the view doesn't allow the creation of recipes with missing data
        for key in keys:
            post_data = {key: self.mock_data[key]}
            response = self.client.post(self.recipes_url, data=post_data, content_type="application/json")
            self.assertEqual(
                response.status_code, 400, f"Should not be able to create a recipe with only '{key}' data"
            )

    def test_list_recipes(self):
        """
        This method tests if the 'list_recipes' method of the view RecipesViewSet is able to return a list of Recipes
        """

        response = self.client.get(self.recipes_url)

        # Checking for status code
        self.assertEqual(response.status_code, 200, "Status code should be 200")

        response_data = response.json()

        # Checking for type of the response
        self.assertTrue(isinstance(response_data, list), "Response object should be a list")

        # Checking for the length of the response
        self.assertGreaterEqual(len(response_data), 1, "Length of the response list should be greater or equal to 1")

        first_element = response_data[0]
        self.assert_dictionaries(data=first_element)

        # Checking if the data matches with what was informed in the setUp function
        self.assertEqual(
            first_element["title"], self.test_recipe.title, f"The title should be '{self.test_recipe.title}'"
        )
        self.assertEqual(first_element["text"], self.test_recipe.text, f"The text should be '{self.test_recipe.text}'")

    def test_get_recipe(self):
        """
        This method tests if the 'get_recipe' method of the RecipesViewSet is able to retrieve a single Recipe from the database with
        a given id in route param
        """
        manage_recipes_url = reverse("core:manage-recipe", kwargs={"recipe_id": self.test_recipe.pk})
        response = self.client.get(manage_recipes_url)

        # Checking for status code
        self.assertEqual(response.status_code, 200, "Status code should be 200")

        response_data = response.json()
        self.assert_dictionaries(data=response_data)

        # Checking if the data matches with what was informed in the setUp function
        self.assertEqual(
            response_data["title"], self.test_recipe.title, f"The title should be '{self.test_recipe.title}'"
        )
        self.assertEqual(response_data["text"], self.test_recipe.text, f"The text should be '{self.test_recipe.text}'")

        nonexistent_id = Recipe.objects.last().pk + 1
        url = reverse("core:manage-recipe", kwargs={"recipe_id": nonexistent_id})
        response = self.client.get(url)

        # Checking if the view isn't trying to fetch something that doesn't exists
        self.assertEqual(response.status_code, 404, "Should not be able to fetch a recipe that doesn't exists")

    def test_update_recipe(self):
        """
        This method tests if the method 'update_recipe' of the RecipesViewSet is able to update a single recipe from the database.
        Also checks if someone is able to update a recipe without informing the recipe's key or if the key is wrong.
        """
        recipe: Recipe = Recipe.objects.create(
            title=self.mock_data["title"], text=self.mock_data["text"], key=self.mock_data["key"]
        )

        put_data = {"title": "A new recipe", "text": "How cool is this recipe?", "key": self.mock_data["key"]}

        manage_recipes_url = reverse("core:manage-recipe", kwargs={"recipe_id": recipe.pk})
        response = self.client.put(manage_recipes_url, data=put_data, content_type="application/json")

        # Checking for the status code
        self.assertEqual(response.status_code, 200, "Status code should be 200")

        # Checking if the values in the database corresponds to what was informed in the request
        recipe = Recipe.objects.get(id=recipe.pk)
        keys = ["title", "text"]
        for key in keys:
            db_value = getattr(recipe, key)
            self.assertEqual(
                db_value, put_data[key], f"The value of '{key}' should be '{put_data['key']}' not '{db_value}'"
            )

        new_data = {"title": "A new title", "text": "A new text"}
        response = self.client.put(manage_recipes_url, data=new_data, content_type="application/json")

        # Checking if the view isn't updating a recipe without informing it's key
        self.assertEqual(response.status_code, 400, "Should not be able to update a recipe without informing the key")

        new_data["key"] = "a different key"
        response = self.client.put(manage_recipes_url, data=new_data, content_type="application/json")

        # Checking if the view isn't updating a recipe without the key being equals to the recipe's key
        self.assertEqual(response.status_code, 400, "Should not be able to update a recipe with the wrong key")

        nonexistent_id = Recipe.objects.last().pk + 1
        url = reverse("core:manage-recipe", kwargs={"recipe_id": nonexistent_id})
        response = self.client.put(url, data=new_data, content_type="application/json")

        # Checking if the view isn't trying to update something that doesn't exists
        self.assertEqual(response.status_code, 404, "Should not be able to update a recipe that doesn't exists")

    def test_delete_recipe(self):
        """
        This method tests if the 'delete_recipe' method of RecipesViewSet is able to delete a single Recipe from the database with a
        given id in route param
        """
        recipe: Recipe = Recipe.objects.create(
            title=self.mock_data["title"], text=self.mock_data["text"], key=self.mock_data["key"]
        )

        manage_recipes_url = reverse("core:manage-recipe", kwargs={"recipe_id": recipe.pk})
        response = self.client.delete(manage_recipes_url)

        # Checking for the status code
        self.assertEqual(response.status_code, 204, "Status code should be 204")

        old_pk = recipe.pk
        recipe = None
        try:
            recipe = Recipe.objects.get(id=old_pk)
        except:
            pass

        # Checking if the Recipe was actually deleted
        self.assertTrue(recipe is None, f"The recipe of id {old_pk} should've been deleted")

        nonexistent_id = Recipe.objects.last().pk + 1
        url = reverse("core:manage-recipe", kwargs={"recipe_id": nonexistent_id})
        response = self.client.delete(url)

        # Checking if the view isn't trying to delete something that doesn't exists
        self.assertEqual(response.status_code, 404, "Should not be able to delete a recipe that doesn't exists")

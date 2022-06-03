from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import RecipesViewSet


class TestUrls(SimpleTestCase):
    def get_assertion_data(self, url: str):
        view_name = resolve(url).func.__name__
        target_name = RecipesViewSet.as_view({"get": "list_recipes"}).__name__
        msg = f"The function '{view_name}' should be '{target_name}'"
        return view_name, target_name, msg

    def test_recipes(self):
        url = reverse("core:recipes")
        view_name, target_name, msg = self.get_assertion_data(url)
        self.assertEqual(view_name, target_name, msg)

    def test_manage_recipe(self):
        url = reverse("core:manage-recipe", kwargs={"recipe_id": 1})
        view_name, target_name, msg = self.get_assertion_data(url)
        self.assertEqual(view_name, target_name, msg)

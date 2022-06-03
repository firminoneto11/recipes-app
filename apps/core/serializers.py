from rest_framework.serializers import ModelSerializer
from .models import Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
        extra_kwargs = {
            "key": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

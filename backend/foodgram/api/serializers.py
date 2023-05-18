from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from recipes.models import Favorite, Ingredient, ShopingCart, Tag
from users.models import UserFoodgram, Recipe, Subscription


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(
        method_name='get_is_subscribed',
        read_only=True
    )

    class Meta:
        model = UserFoodgram
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        ]

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        user = request.user
        return Subscription.objects.filter(
            following=obj,
            follower=user
        ).exists()


class CustomUserCreateSerializer(UserCreateSerializer):
    pass


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
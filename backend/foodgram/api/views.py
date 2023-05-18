from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import filters, status, viewsets
from djoser.views import UserViewSet
from .serializers import CustomUserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer

    @action(['get'], detail=False, permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        return self.retrieve(request, *args, **kwargs)

class FavoriteViewSet(viewsets.ModelViewSet):
    pass


class IngredientsViewSet(viewsets.ModelViewSet):
    pass


class RecipesViewSet(viewsets.ModelViewSet):
    pass


class TagsViewSet(viewsets.ModelViewSet):
    pass


class UsersViewSet(viewsets.ModelViewSet):
    pass


class SubscriptionsViewSet(viewsets.ModelViewSet):
    pass


class ShoppingCartViewSet(viewsets.ModelViewSet):
    pass

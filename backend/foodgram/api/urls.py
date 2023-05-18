from api.views import (FavoriteViewSet, IngredientsViewSet, RecipesViewSet,
                    TagsViewSet, UsersViewSet, SubscriptionsViewSet, 
                    ShoppingCartViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()

router.register('tags', TagsViewSet, basename='tags')
router.register('recipies', RecipesViewSet, basename='recipes')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register(r'users', UsersViewSet, basename='users')
router.register(
    r'recipies/download_shopping_cart/', ShoppingCartViewSet, basename='shopping_cart'
)
router.register(
    r'recipies/(?P<recipies_id>\d+)/favorite', FavoriteViewSet, basename='favorite'
)
router.register(
    r'users/subscriptions', SubscriptionsViewSet, basename='subscribtions'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]

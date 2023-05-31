from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (IngredientViewSet, RecipeViewSet, SubscribeView,
                       SubscriptionViewSet, TagViewSet, UserFoodgramViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register(
    r'users/subscriptions',
    SubscriptionViewSet,
    basename='subscriptions'
)
router.register(r'users', UserFoodgramViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/subscribe/', SubscribeView.as_view()),
    path('auth/', include('djoser.urls.authtoken')),
]

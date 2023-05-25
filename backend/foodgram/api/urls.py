from api.views import (IngredientViewSet, RecipeViewSet,
                       TagViewSet, UserFoodgramViewSet, SubscriptionViewSet,
                       SubscribeView)
from django.urls import include, path
from rest_framework.routers import DefaultRouter


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
    path('auth/', include('djoser.urls.authtoken')),
    path('users/<int:pk>/subscribe/', SubscribeView.as_view()),
]

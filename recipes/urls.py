from django.urls import path

from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view(), name='recipes.list'),
    path('recipes/new/', views.RecipeCreateView.as_view(), name='recipes.new'),
    path('recipes/popular/', views.RecipePopularListView.as_view(), name='recipes.popular'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes.detail'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipes.update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipes.delete'),
    path('recipes/<int:pk>/share/', views.RecipeShareView.as_view(), name='recipes.share'),
    path('recipes/<int:pk>/add-like/', views.add_like, name='recipes.add_like'),
    path('recipes/<int:pk>/mark-private/', views.mark_private, name='recipes.mark_private'),
    path('recipes/<int:pk>/mark-public/', views.mark_public, name='recipes.mark_public'),
]
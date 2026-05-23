from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipes.list')
    template_name = 'recipes/recipes_form.html'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-updated_at')


class RecipePopularListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_popular.html'
    context_object_name = 'recipes'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(is_public=True).order_by('-likes', '-updated_at')


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipe'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(Q(author=self.request.user) | Q(is_public=True))


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipes_form.html'
    success_url = reverse_lazy('recipes.list')
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipes_delete.html'
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipes.list')
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class RecipeShareView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_share.html'
    context_object_name = 'recipe'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(Q(author=self.request.user) | Q(is_public=True))


def add_like(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.likes = F('likes') + 1
    recipe.save(update_fields=['likes'])
    return redirect('recipes.detail', pk=pk)


def mark_private(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    recipe.is_public = False
    recipe.save(update_fields=['is_public'])
    return redirect('recipes.share', pk=pk)


def mark_public(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    recipe.is_public = True
    recipe.save(update_fields=['is_public'])
    return redirect('recipes.share', pk=pk)
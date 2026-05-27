from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = '/smart/recipes'
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
        return Recipe.objects.filter(
            Q(is_public=True) | Q(author=self.request.user)
        ).order_by('-is_public', '-created_at')


class RecipePopularListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_popular.html'
    context_object_name = 'recipes'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(
            Q(likes__gte=1),
            Q(is_public=True) | Q(author=self.request.user),
        ).order_by('-likes', '-updated_at', '-created_at')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipe'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recipe.objects.filter(Q(author=self.request.user) | Q(is_public=True))

        return Recipe.objects.filter(is_public=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']
        context['is_owner'] = (
            self.request.user.is_authenticated and recipe.author_id == self.request.user.id
        )
        return context


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipes_form.html'
    success_url = '/smart/recipes'
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


class RecipeShareView(DetailView):
    model = Recipe
    template_name = 'recipes/recipes_share.html'
    context_object_name = 'recipe'

    def get_object(self, queryset=None):
        return Recipe.objects.filter(pk=self.kwargs['pk']).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context.get('recipe')

        if recipe is None:
            context['show_not_found_message'] = True
            context['can_view_recipe'] = False
            context['is_owner'] = False
            return context

        is_owner = self.request.user.is_authenticated and recipe.author_id == self.request.user.id
        can_view_recipe = recipe.is_public or is_owner

        context['show_not_found_message'] = not can_view_recipe
        context['can_view_recipe'] = can_view_recipe
        context['is_owner'] = is_owner
        context['share_url'] = self.request.build_absolute_uri(
            reverse('recipes.detail', kwargs={'pk': recipe.pk})
        )
        return context


class AuthorRecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    login_url = '/login'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-created_at')


@login_required(login_url='/login')
def add_like(request, pk):
    recipe = get_object_or_404(
        Recipe,
        Q(pk=pk),
        Q(is_public=True) | Q(author=request.user),
    )
    recipe.likes = F('likes') + 1
    recipe.save(update_fields=['likes'])
    recipe.refresh_from_db(fields=['likes'])
    return redirect('recipes.detail', pk=pk)


@login_required(login_url='/login')
def mark_private(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    recipe.is_public = False
    recipe.save(update_fields=['is_public'])
    recipe.refresh_from_db(fields=['is_public'])
    return redirect('recipes.share', pk=pk)


@login_required(login_url='/login')
def mark_public(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    recipe.is_public = True
    recipe.save(update_fields=['is_public'])
    recipe.refresh_from_db(fields=['is_public'])
    return redirect('recipes.share', pk=pk)
from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-5', 'rows': 3}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control my-5', 'rows': 4}),
            'instructions': forms.Textarea(attrs={'class': 'form-control my-5', 'rows': 5}),
        }
        labels = {
            'title': 'Recipe Title',
            'description': 'Short Description',
            'ingredients': 'Ingredients (one per line)',
            'instructions': 'Cooking Instructions',
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')

        return title
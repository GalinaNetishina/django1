from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    pages = {
        dish: f'{dish}/'
        for dish in DATA.keys()
    }
    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def recipe_view(request, dish):
    amount = int(request.GET.get('servings', '1'))

    recipe = {item: amount*value for item, value in DATA.get(dish, {}).items()}
    return render(request, 'calculator/index.html', context={'recipe': recipe})

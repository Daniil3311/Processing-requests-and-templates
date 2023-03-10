from django.http import HttpResponse
from django.shortcuts import render


def omlet(request):
    template_name = 'calculator/index.html'
    servings=int(request.GET['servings'])
    context = {'recipe': {
        'молоко, л': (f'{0.1*servings}'),
        'яйца, шт': (f'{2*servings}'),
        'соль, ч.л.': (f'{0.5*servings}'),
    },
    }
    return render(request, template_name, context)


def pasta(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET['servings'])
    context={'recipe': {
        'макароны, г': (f'{0.3*servings}'),
        'сыр, г': (f'{0.05*servings}'),
    }
    }
    return render(request, template_name, context)


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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:








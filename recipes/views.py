from django.shortcuts import render

def home(request):
    return render(request, template_name= 'recipes/pages/home.html', context={
        
        'name': 'leonardo'
})


def recipe(request, id):
    return render(request, template_name= 'recipes/templates/pages/recipe-view.html', context={
        
        'name': 'leonardo'
})
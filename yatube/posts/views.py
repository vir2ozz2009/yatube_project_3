from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
#def index(request):    
#    return HttpResponse('Главная страница')

def index(request):
    template = 'posts/index.html'
    return render(request, template) 

# Страница со списком мороженого
def group_posts(request):
    return HttpResponse('Группы')
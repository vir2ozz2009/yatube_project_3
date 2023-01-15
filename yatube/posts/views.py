from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


#def index(request):
#    template = 'posts/index.html'
#    text = 'Это главная страница проекта Yatube'
#    context = {
#        'text1': text,
#    }
#    return render(request, template, context) 

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

# Страница со списком мороженого
#def group_posts(request):
#    return HttpResponse('Группы')

def group_list(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text2': text,
    }
    return render(request, template, context)
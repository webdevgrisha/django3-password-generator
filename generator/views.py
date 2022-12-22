from django.shortcuts import render  # функция из фрэемворка django, позволяет возвращать шаблоны в виде HttpResponse
from django.http import HttpResponse  # импортируем модуль HttpResponse из фрэимворка django
import random


# Create your views here.
# функция которая будет вызвана в фале urls.py
def home(request):  # request - это то что ищет пользователь
    # мы не можем вернуть обычную строку ответ на зарпрос должен быть в формате Http

    # шаблоны используются для упрощения создания  дезайна websites, отвечают только за визуальное отображение
    # они позволяют в специфичном формате отображать HTML код, который будет интерпретироваться браузером
    # в зависемости от назначения сайта мы можем использовать различные шаблоны, подходящие именно нам
    # для работы с шаблонами на нужно создать папку в каталоге нашего проекта
    # для каждого шаблона нужно создавать отдельную папку в котором будет описание конктрентного приложения
    # это все чтобы не запутаться в структуре проекта
    return render(request, 'generator/home.html')
    # параметр request который к нам пришел в функцию home передаем в кутвук
    # через запятую добавляем путь к шаблону
    # мы можем передавать информацию из views.py в шаблоны
    # для это через "," в "{}" скобка добавляем значение


def about(request):
    return render(request, 'generator/about.html')


# вся информация из формы содержится в прараметре request, это предустановка django
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    #
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-/<>.\|[]{}~``'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # данная переменная берет значение из адресной сторки
    # заначение будет взято из тэга select с именем length
    # таким образом будет происходить поиск и других переменных, значения будут взяты согласно параметрам команды
    # можно использовать значение по умолчанию для команды get
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

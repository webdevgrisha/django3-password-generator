"""password_gnerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# данный файл это точка отсчета любого jango проекта
# строки которые мы набираем в адресной строке браузера будет передана в данный файл
# здесь определяется все дальнейшее поведение по переходам по сайту
# здесь хранятся все urls ссылки которые привязаны к нашему сайту
# чтобы добавить возможные варианты адресса сайта мы идем в urls.py
# в urls.py просходит поиск заданого имени сайта
# маршрутезация на сатйте происходить через файл urls.py

# // Пример жизненого цикла запросов в мире django !
# кто-то набирает адрес в адресной строке
# далее он попадает в urls.py, где ищет совподения по этому запросу
# после этого он будет переадресован на функцию views.home
# views.home оправляет зарпрос в views.py, где содержится функция home
# которая выполняет команду render home.html и добавляет туда информацию из словаря password
# проследовав в home.html наш запрос считывает из него специфический формат, изменяя password на значение из словаря
# которая в ответ на запрос, возваращает данные преобразуемые в то, что мы видем на запрощенной странице
# и пользователь получает результат в браузере


from django.urls import path
from generator import views  # импортируем файл views из папки generator

urlpatterns = [
    # в jango адресса определяются функцие path, которая принемает содержание адрессной строки вводимой пользователям

    # path('url адрес в адрессной строке')
    path('', views.home, name='home'),
    # '' - адресс домашней страницы, может на конце содержать "/"
    # если мы хотим отобразить конкретную страницу нужна после '', добавить конкретное значение которое мы хотим вернуть в ответ на запрос
    # в нашем случае мы хотим отобразить одну из страниц которые будут содержаться в папке generator в файле views.property
    # при запросе на домашнию страницу мы вернем views которая будет иметь имя home
    # django отобразит специальную страницу если в urls.py не находит адресса указаного в качестве домашнего
    path('password', views.password, name='password'),
    path('about', views.about, name='about')
]
# '' - адрес домашней страницы

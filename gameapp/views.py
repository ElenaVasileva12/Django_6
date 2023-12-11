from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Coin
from .forms import GameCoinForm


# � Создайте представление “Привет, мир!” внутри вашего
# первого приложения
def index(request):
    return HttpResponse('Привет, мир!')

# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
def coin(request,count=5):
    lst=[]
    for i in range(count):
        site=choice(['Орел','Решка'])
        lst.append(site)
    context={'game_name':'Орел и Решка','value':lst}
    #site=choice(['Орел','Решка'])
   # value=Coin(site=site)
   # value.save()             #http://127.0.0.1:8088/game/coin/
   # return HttpResponse(str(site))
    return render(request,'gameapp/game.html',context=context)

def cub(request,count=5):
    lst=[]
    for i in range(count):
        s=str(randint(1,7))
        lst.append(s)
    context={'game_name':'Кубик','value':lst}
   # return HttpResponse(str(randint(1,7)))
    return render(request,'gameapp/game.html',context=context)

def numbers(request,count=5):
    lst=[]
    for i in range(count):
        s=str(randint(1,101))
        lst.append(s)
    context={'game_name':'Случайное число','value':lst}
    return render(request,'gameapp/game.html',context=context)
    #return HttpResponse(str(randint(1,101)))

def coin_values(request):
    value=Coin.values()
    print(value)
    lst=[]
    for i in value:
        print(i)
        lst.append(i)
    return HttpResponse(lst)

def dice(request):
    pass

def game_choice(request):
    if request.method == 'POST':
        form=GameCoinForm(request.POST)
        if form.is_valid():
            game=form.cleaned_data['game']
            size=form.cleaned_data['size']
            if game =='coin':
                return coin(request,size)
    else:
        form=GameCoinForm()
    return render(request,'gameapp/game.html',{'form':form})
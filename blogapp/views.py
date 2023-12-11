from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
from .forms import AutorForms

    # name=models.CharField(max_length=100)
    # secondname=models.CharField(max_length=100)
    # email=models.EmailField()
    # bio=models.TextField()
    # bday=models.DateField()



def index(requests):
    return HttpResponse('Hello')

def view_autor(requests):
    #фейковые данные
    for i in range(101):
        autor=Autor(name=f'aaa{i}', secondname=f'bbb{i}',email=f'aaa@{i}.ru',bio=f'cccc{i}', bday=f'2023-11-23')
        autor.save()
    return HttpResponse('autor')

def post_autor(request):
    if request.method == 'POST':
        form = AutorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            secondname = form.cleaned_data['secondname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            bday = form.cleaned_data['bday']
            autor=Autor(name=name,
                        secondname=secondname,
                        email=email,
                        bio=bio,
                        bday=bday)
            autor.save()
            return render(request, 'blogapp/postautor.html', {'answer':'Автор добавлен'})

    else:
        form = AutorForms()
    return render(request, 'blogapp/postautor.html', {'form':form})


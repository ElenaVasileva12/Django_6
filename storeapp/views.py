from django.shortcuts import render
from django.http import HttpResponse
from .models import Client,Product,Order
from datetime import datetime, timedelta,date
from .forms import ProductsForms,my_list,TitleForms
from django.core.files.storage import FileSystemStorage



def index(request):
    if request.method == 'POST':
        form=TitleForms(request.POST)
        if form.is_valid():
            categories=form.cleaned_data['categories']
            if categories =='prod':
                return post_product(request) #изменить продукты
            elif categories=='ord':
                return view_client(request) #заказы
    else:
        form=TitleForms()
    return render(request,'storeapp/title.html',{'form':form})


def view_client(requests):
    #фейковые данные
    for i in range(11):
        client=Client(name=f'client_{i}', 
                      email=f'client{i}@mail.ru', 
                      phone=f'1234567{i}',
                      address=f'Академика Каралева, {i}',
                      day_reg=f'2027-11-23 11:00')
        client.save()
        Client.objects.all()
    for i in range(101):
        product=Product(name=f'product_{i}', 
                        description=f'product_desc{i}',
                        prise=i**2,
                        count_product=i,
                        date_create=f'2027-11-23 11:00')
        product.save()

       
    #Данные для many to many
    product1=Product(name=f'Блины', 
                        description=f',bn,bn,nb,bn,',
                        prise=555,
                        count_product=7,
                        date_create=f'2023-11-2 11:00')
                        
    product1.save()
    product2=Product(name=f'Каша', 
                        description=f'hjkhj',
                        prise=2,
                        count_product=3,
                        date_create=f'2023-09-25 11:00')
    product2.save()
    product3=Product(name=f'Борщ', 
                        description=f'jjjjjjj',
                        prise=54,
                        count_product=24,
                        date_create=f'2023-03-07 11:00')
    product3.save()
    Product.objects.all()

# #создали заказы
    order1=Order(customer_id=10,
                  total_price=45,
                  date_ordered=f'2023-12-02'
                  )
    order1.save()
    
    order2=Order(customer_id=7,
                 total_price=15,
                date_ordered=f'2023-11-01'
                )
    order2.save()

    order3=Order(customer_id=2,
                 total_price=25,
                date_ordered=f'2023-11-04'
                )
    order3.save()
   
#Выбираем данные из order
    e1=Order.objects.filter(customer_id=10).first()
    e2=Order.objects.filter(customer_id=7).first()
    e3=Order.objects.filter(customer_id=2).first()
  
    #Добавляем к заказу продукты
    e1.products.add(product1)
    e1.products.add(product2)
    e1.products.add(product3)
    e1.save()
    e1.products.all()

    e2.products.add(product1)
    e2.products.add(product2)
    e2.save()
    e2.products.all()

    e3.products.add(product1)
    e3.products.add(product3)
    e3.save()
    e3.products.all()


    context={'Клиент':e1.customer,'Заказы':e1.products.all}
   # return HttpResponse('Данные загружены')
    return render(requests,'storeapp/client.html',context=context)

#За определенный день
def view_client_day(requests,day_):
    # ищем данные за определенное количество дней (что введем в day_)
    now_=datetime.now()
    min_=now_ - timedelta(days=day_)

#Выбираем данные из order
    e1=Order.objects.filter(customer_id=10,date_ordered__range=(min_, now_)).first()
    e2=Order.objects.filter(customer_id=7,date_ordered__range=(min_, now_)).first()
    e3=Order.objects.filter(customer_id=2,date_ordered__range=(min_, now_)).first()

  
    #Добавляем к заказу продукты

    e1.products.all()
    e2.products.all()
    e3.products.all()

    context={'Клиент':e1.customer,'Заказы':e1.products.all}
   # return HttpResponse('Данные загружены')
    return render(requests,'storeapp/client2.html',context=context)

#изменение данных о продукте
def post_product(request):
    if request.method == 'POST':
        form = ProductsForms(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            prise = form.cleaned_data['prise']
            count_product = form.cleaned_data['count_product']
            date_create = form.cleaned_data['date_create']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()

            prod=Product(id=name,
                        name=name,
                        description=description,
                        prise=prise,
                        count_product=count_product,
                        date_create=date_create)
            prod.save(update_fields=["description",'prise','count_product','date_create'])
            fs.save(image.name, image)
            return render(request, 'storeapp/poduct.html', {'answer':'Продукт изменен'})
    else:
        form = ProductsForms()
    return render(request, 'storeapp/product.html', {'form':form})
from django.contrib import admin
from .models import Client,Product,Order

# Настройте под свои нужды вывод информации о клиентах, 
# товарах и заказах на страницах вывода информации об объекте 
# и вывода списка объектов.

#меняем  поле name на test
@admin.action(description="тестовая активность")
def admintest(modeladmin,request, queryset):
    queryset.update(name='test')

@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, count_product):
    count_product.update(count_product=0)


class AdminClient(admin.ModelAdmin): #настройка админа фильсты
    list_display=('name','email','phone') 
    list_filter=('name',)
    search_fields=('phone',)
    """Отдельный продукт."""
   # fields = ['name', 'secondname'] #поля которые будут отображаться при кликуаньи
   # readonly_fields = ['name', 'secondname','bday']

    fieldsets = [('Тест',{'fields': ['name', 'email']}),
                 ('Тест2',{'fields': ['address', 'phone']})]
    actions=[admintest]

admin.site.register(Client,AdminClient) #подключаем модель в админ

class AdminProduct(admin.ModelAdmin): #настройка админа фильсты
    list_display=('name','description','prise','count_product') 
    list_filter=('count_product',)
    search_fields=('date_create',)
    """Отдельный продукт."""
   # fields = ['name', 'secondname'] #поля которые будут отображаться при кликуаньи
   # readonly_fields = ['name', 'secondname','bday']

    fieldsets = [('Тест',{'fields': ['name', 'description']}),
                 ('Тест2',{'fields': ['prise', 'count_product']})]
    actions=[admintest]
    actions=[reset_count]
admin.site.register(Product,AdminProduct) #подключаем модель в админ


class AdminOrder(admin.ModelAdmin): #настройка админа фильсты
    list_display=('customer','date_ordered') 
    list_filter=('total_price',)
    search_fields=('total_price',)
    """Отдельный продукт."""
   # fields = ['name', 'secondname'] #поля которые будут отображаться при кликуаньи
   # readonly_fields = ['name', 'secondname','bday']

    fieldsets = [('Тест',{'fields': ['customer', 'date_ordered']}),
                 ('Тест2',{'fields': ['products', 'total_price']})]
    
admin.site.register(Order,AdminOrder) #подключаем модель в админ
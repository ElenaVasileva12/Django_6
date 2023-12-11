from django.contrib import admin
from .models import Autor

# Register your models here.
# Проверьте возможность доступа к админке.
# Создайте суперпользователя и войдите в админ панель

# Подключите к админ панели созданные вами в рамках
# прошлых семинаров модели в приложениях:
# ○ случайные числа,
# ○ блог,
# ○ магазин,
# ○ другие, если вы их создавали.



# Настройте под свои нужды вывод информации об авторах,
# статьях и комментариях на страницах списков.

#меняем  поле name на test
@admin.action(description="тестовая активность")
def admintest(modeladmin,request, queryset):
    queryset.update(name='test')

class AdminAutor(admin.ModelAdmin): #настройка админа фильсты
    list_display=('name','secondname','bday') #чтобы время не отображалось, только site
    list_filter=('secondname',)
    search_fields=('secondname',)
    
    """Отдельный продукт."""
   # fields = ['name', 'secondname'] #поля которые будут отображаться при кликуаньи
   # readonly_fields = ['name', 'secondname','bday']


# Настройте под свои нужды вывод информации об авторах,
# статьях и комментариях на страницах вывода информации
# об объекте.
    fieldsets = [('Тест',{'fields': ['name', 'secondname']}),
                 ('Тест2',{'fields': ['email', 'bday']})]

    actions=[admintest]

admin.site.register(Autor,AdminAutor) #подключаем модель в админ
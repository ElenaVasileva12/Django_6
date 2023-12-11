from django.contrib import admin
from .models import Coin

# Register your models here.
class AdminCoin(admin.ModelAdmin): #настройка админа фильсты
    list_display=('site',) #чтобы время не отображалось, только site



admin.site.register(Coin,AdminCoin) #подключаем модель в админ

from django import forms
from .models import Product
from datetime import datetime,date
from django.forms.widgets import Select


# Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# Создайте форму для редактирования товаров в базе
# данных.

#функция для выпадающего списка из базы данных
def pr_val():
    pr_values=[]
    pr_list = Product.objects.all().order_by('id', 'name')
    for pr in pr_list:
        pr_values.append((pr.id, pr.name))
    return pr_values

my_list=pr_val()
PRODUCT_CHOICES=(my_list)

class ProductsForms(forms.Form):
    name=forms.CharField(widget=forms.Select(choices=PRODUCT_CHOICES))
    description=forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control'}))
    prise=forms.FloatField(min_value=0)
    count_product=forms.IntegerField(min_value=1)
    date_create=forms.DateField(initial=date.today)
    image = forms.ImageField()


class TitleForms(forms.Form):
    categories=forms.ChoiceField(choices=(('prod','Продукты'),('ord','Заказы')))





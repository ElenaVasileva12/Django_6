from django.db import models

# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов. 
# Заказ может содержать несколько товаров. 
# Товар может входить в несколько заказов.

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

# Допишите несколько функций CRUD для работы с моделями по желанию. 
# Что по вашему мнению актуально в такой ба

class Client(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    address=models.TextField()
    day_reg=models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.email}'
    

class Product(models.Model):
    name=models.CharField(max_length=100) # ,unique=True уникальный продукт
    description=models.TextField()
    prise=models.DecimalField(max_digits=8, decimal_places=2)
    count_product=models.IntegerField()
    date_create=models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.name} {self.prise} {self.count_product}'
    

class Order(models.Model):
    customer = models.ForeignKey(to='Client',on_delete=models.CASCADE)
    products = models.ManyToManyField(to='Product',db_table='storeapp_orderproduct')  #https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
    date_ordered = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2,default=1)
    
    def __str__(self):
        return f'{Client.name} {self.date_ordered}'
from django.db import models

# Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное
# имя”, которое возвращает имя и фамилию.

class Autor(models.Model):
    name=models.CharField(max_length=100)
    secondname=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()
    bday=models.DateField()

    def __str__(self):
        return f'{self.name} {self.secondname}'
    


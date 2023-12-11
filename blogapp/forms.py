# Семинар 4

# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author

from django import forms
from .models import Autor

class AutorForms(forms.ModelForm):
    class Meta:
        model=Autor
        fields=['name', 'secondname', 'email', 'bio', 'bday']

 

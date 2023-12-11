from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime

# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html —
# многострочный текст с HTML-вёрсткой и данными о вашем 
# первом Django-сайте и о вас.

# Сохраняйте в логи данные о посещении страниц.
logger = logging.getLogger(__name__)

def title(request): 
    context={'name':'dfgdfg','age':56,'lastname':'gggggg'}
    # html = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>О себе</title>
    #     <style>
    #         body {
    #             font-family: Arial, sans-serif;
    #             line-height: 2.5;
    #             margin: 0;
    #             padding: 20px;
    #         }
            
    #         h1 { color: #278;}
            
    #         p {color: #658; }
    #     </style>
    # </head>
    # <body>
    #     <h1>Django сайт</h1>
    
    #     <p>Django - это высокоуровневый фреймворк для веб-приложений на языке
    #     Python. Он был создан в 2005 году и с тех пор активно развивается и
    #     обновляется сообществом разработчиков по всему миру</p>
    # <h2>Преимущества использования Django</h2>
    #     <p>Использование Django имеет множество преимуществ, таких как:</p>
    #     <p>● Быстрая разработка веб-приложений</p>
    #     <p>● Простота и удобство использования</p>
    #     <p>● Высокая производительность</p>
    #     <p>● Безопасность</p>
    #     <p>● Масштабируемость</p>
    # </body>
    # </html>
    # """
    logger.info(f'Visiting a page TITLE in: {datetime.now()}')
   # return HttpResponse(html)
    return render(request,template_name='homeapp/index.html',context=context)

def my_site(request): 
    # html = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>О себе</title>
    #     <style>
    #         body {
    #             font-family: Arial, sans-serif;
    #             line-height: 2.5;
    #             margin: 0;
    #             padding: 20px;
    #         }
    #         h1 { color: #25;}
    #         p {color: #999; }
    #     </style>
    # </head>
    # <body>
        
    # <h1>О себе</h1>
    #     <p>Меня зовут Васильева Елена. Мне 38 лет и проживаю в городе Тюмень.
    #     Я имею высшее образование в области информационных технологий. 
    #     Работаю по специальности. Хочу получить дополнительные навыки</p>
    #    </body>
    # </html>
    # """
    logger.info(f'Visiting a page MY_SITE in: {datetime.now()}')
 #   return HttpResponse(html)
    return render(request,template_name='homeapp/two_index.html')

#http://127.0.0.1:8088/title/
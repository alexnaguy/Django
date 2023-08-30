from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from random import randint
from abc import ABC, abstractmethod


class Page:
 
    def view_hello(request):
            
            return HttpResponse(f"""
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>  Hello, World! </h1>
                    <p> Меня зовут Алекс и это моя первая страница на django! </p>
                </body>
            </html>
            """)
    


    def view_day_week(request):
         
         day_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
        }
         

         day_number = datetime.now().weekday()

         return HttpResponse(f"""
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>  Сегодня {day_week[day_number]} </h1>
                    
                </body>
            </html>
            """)
        #  return HttpResponse(f"Сегодня {day_week[day_number]}")


    def random_title(request):

        quotes = {
             
             1: "Чем дольше будешь ждать, тем больше дней ты потеряешь навсегда.",
             2 : "Дорога под названием потом ведет в страну под названием никуда.",
             3: "Вы видите мою одежду, но не мою душу.Вы знаете мое имя, но не мою историю.",
             4: "Виноваты, конечно, всегда другие…",
             5: "Хуже каменного сердца может быть только жидкий мозг.",

              
         }
        number = randint(1, 5)
        return HttpResponse(quotes[number])
        

        
        
         
class Page_two:

    def show_time(request):
          
        date = str(datetime.now().date())
        time = str(datetime.now().time())[:-7]
        return HttpResponse(f"Дата: {date } Время: {time}")
           

    def multi_table(response):
        
        table = ''
        for i in range(1, 10):
            for j in range(1, 10):
                table += f'<p>{i} x {j} = {i * j}</p>'
            table += '<hr>'
        return HttpResponse(table)
    




class TemplateWebSite(ABC):

    @abstractmethod
    def main(request):
        return HttpResponseNotFound(f"""
        <!DOCTYPE html>
        <html>
            <head></head>
            <body>
                <h1> 404 ERROR: PAGE NOT FOUND ! </h1>
            </body>
        </html>
        """)
    
    @abstractmethod
    def news_city(request):
        return HttpResponseNotFound("Not Found")

    @abstractmethod
    def managers_city(request):
        return HttpResponseNotFound("Not Found")

    @abstractmethod
    def facts_city(request):
        return HttpResponseNotFound("Not Found")
    
    @abstractmethod
    def contacts(request):
        return HttpResponseNotFound("Not Found")
    
    @abstractmethod
    def history(request):
        return HttpResponseNotFound("Not found")
    

class Article:

    def __init__(self, title, author, desc) -> None:
        self.title = title
        self.author = author
        self.desc = desc


class NewCity (TemplateWebSite):

    def main(request):
        return render(request, 'main.html', {
            "name": "Москва",
        })
    


    def news(request):
        
        return render(request, 'news.html', {
            "news_list": ["Новость 1", "Новость 2", "Новость 3"]
        })


    def managers_city(request):

        return render(request, "managers.html" )
    

    def facts_city(request):
        return render(request, "facts.html")
    
    
    def contacts(request):
        return render(request, "contacts.html")
    
    def history(request, page):
        if not page:
            return render(request, f'history/historym.html' )
        
        return render(request, f'history/{page}.html' )
    

    
    


    

        
    
    


    
        




     



      
     
    

   
    







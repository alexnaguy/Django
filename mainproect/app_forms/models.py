from django.db import models

class Articles(models.Model):
    tittle = models.CharField('Название', max_length= 100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField("Дата публикации")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Cars(models.Model):
    #name, url, price, description, date_car_par
    name = models.CharField('Название объявления', max_length= 300)
    url = models.URLField('Сылка')
    price = models.CharField('Цена автомобиля', max_length= 100)
    description = models.TextField('Описание обявления')
    date_car_par = models.CharField('Дата публикации объявления', max_length= 70)


    def __str__(self):
        return self.name





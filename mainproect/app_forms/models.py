from django.db import models

class Articles(models.Model):
    tittle = models.CharField('Название', max_length= 100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

from django.db import models


class PollModel(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    about = models.TextField(verbose_name='Описание')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата старта')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title

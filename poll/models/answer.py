from django.db import models


class AnswerModel(models.Model):
    title = models.CharField(max_length=32, verbose_name='Ответ')
    question = models.ForeignKey('QuestionModel', blank=False, null=False, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='Вопрос')

    class Meta:
        db_table = 'answers'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.title

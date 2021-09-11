from django.db import models


class QuestionModel(models.Model):
    class TypeOfQuestion:
        SINGLE = 0
        MULTIPLE = 1
        TEXT = 2

        CHOICES = (
            (SINGLE, 'RadioButton'),
            (MULTIPLE, 'CheckBox'),
            (TEXT, 'TextBox'),
        )

    title = models.CharField(max_length=256, blank=False, null=False, verbose_name='Вопрос')
    type = models.IntegerField(choices=TypeOfQuestion.CHOICES, blank=False, default=TypeOfQuestion.SINGLE,
                               verbose_name='Тип')
    poll = models.ForeignKey('PollModel', blank=False, null=False, on_delete=models.CASCADE, related_name='questions',
                             verbose_name='Опрос')

    class Meta:
        db_table = 'questions'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title

from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    autor = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return f'{self.autor}:{self.quote[:20]}...'


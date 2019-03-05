from django.db import models

class DNAStrings(models.Model):
    dnaString = models.CharField(max_length=60)
    mutation = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s' % (self.dnaString)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Cadena'
        verbose_name_plural = 'Cadenas'
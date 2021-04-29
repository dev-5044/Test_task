from django.db import models 
from django.utils.translation import gettext_lazy as _ 
from bot.bin_logic import LIMIT, QUANTITY

STATUS = (
    ('OPEN', 'OPEN'),
    ('CLOSE', 'CLOSE'),
    ('ERROR', 'ERROR'),
)


class Asset(models.Model):
    """Модель актива для торговли"""
        
    name = models.CharField(verbose_name='название', max_length=255)
    product = models.CharField(max_length=20, default='BTCUSDT')
    limit = models.FloatField(verbose_name='граница изменения цены',
                                default=0)
    quantity = models.IntegerField(verbose_name='количество', default=0)
    price = models.FloatField(verbose_name='цена', default=0)
    status = models.CharField(choices=STATUS, max_length=10, default='OPEN')
    ma = models.FloatField(default=0)
    work = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Asset, self).save(*args, **kwargs)
        LIMIT.value = self.limit
        QUANTITY.value = self.quantity
                
    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'

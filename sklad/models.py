from django.db import models

# Create your models here.

class Sklad(models.Model):
    storages = (
        ('zabor', 'Забор'),
        ('trotuarka', 'Тротуарка'),
        # ('monuments', 'Памятники')
    )
    storage = models.CharField(
        max_length=10,
        choices=storages, 
        help_text='Name of storage',
        default='trotuarka'
    )

    class Meta:
        verbose_name_plural = 'Склад'
        verbose_name = 'Склад'

    def __str__(self):
        return self.get_storage_display()


class Materials(models.Model):
    sklad = models.ForeignKey(Sklad, on_delete=models.CASCADE)
    pesok = models.IntegerField(verbose_name='Песок т.')
    cement = models.IntegerField(verbose_name='Цемент т.')
    scheben = models.IntegerField(verbose_name='Щебень т. ')
    zavoz = models.DateField(verbose_name='Дата завоза', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Материалы"
        verbose_name = "Материал"

    
class Izdelie(models.Model):
    sklad = models.ForeignKey(Sklad, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    amount = models.IntegerField(verbose_name='Количество', help_text='Для заборов и памятников указывается количество изделий. Для плитки - квадратов')
    
    def getsklad(self):
        return self.sklad.storage
        
    class Meta:
        abstract = True


class Zabor(Izdelie):
    names = (
        ('fagot', 'Фагот'),
        ('krim', 'Крым'),
        ('but', 'Бут'),
    )
    name = models.CharField(
        max_length=15, 
        choices=names, 
        verbose_name='Название изделия',
    )

    def __str__(self):
        return self.get_name_display()
    
    class Meta:
        verbose_name_plural = "Заборы"
        verbose_name = "Забор"


class Trotuarka(Izdelie):
    names = (
        ('st_gor', 'Старый Город'),
        ('kirpichik', 'Кирпичик'),
        ('romb', 'Ромб')
    )
    name = models.CharField(
        max_length=15, 
        choices=names, 
        verbose_name='Название изделия', 
    )

    colors = (
        ('GR', 'Серый'),
        ('BR', 'Коричневый'),
        ('YE', 'Жёлтый'),
        ('OL', 'Оливковый'),
        ('BL', 'Синий'),
        ('RED', 'Красный')
    )
    color = models.CharField(
        max_length=15,
        choices=colors,
        default='GR',
        verbose_name='Цвет'
    )

    def __str__(self):
        return self.get_name_display()
    
    class Meta:
        verbose_name_plural = "Тротуарная плитка"
        verbose_name = "Тротуарная плитка"



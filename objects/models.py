from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Пласт
class Layer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название пласта')

    def __str__(self) -> str:
        return str(self.name)


# Скважина
class Well(models.Model):
    name = models.CharField(max_length=200, verbose_name='Номер скважины')
    layer = models.ForeignKey(
        Layer,
        related_name='layers',
        verbose_name='Пласт',
        on_delete=models.CASCADE,  
        default = 1
    )

    def __str__(self) -> str:
        return str(self.name)   


# Месторождение
class OilField(models.Model): 
    name = models.CharField(max_length=200, verbose_name='Название месторождения')
    well = models.ForeignKey(
        Well,
        related_name='fields',
        verbose_name='Скважина',
        on_delete=models.CASCADE,  
        default = 1
    )

    def __str__(self) -> str:
        return str(self.name)


# Лаборатория
class Lab(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.IntegerField(verbose_name='Номер лаборатории')
    address = models.CharField(max_length=200, verbose_name='Адрес лаборатории')
    def __str__(self) -> str:
        return str(self.name)


# Объект
class Object(models.Model):
    name = models.IntegerField(verbose_name='Номер объекта')
    oilfield = models.ForeignKey(
        OilField,
        related_name='objects',
        verbose_name='Номер месторождения',
        on_delete=models.CASCADE,  
        default = 1
    )
    income_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления в лабораторию')
    date_selection = models.DateTimeField(verbose_name='Дата отбора пробы')
    rock_name = models.CharField(max_length=200, verbose_name='Название породы')
    link_verge3d = models.CharField(max_length=200, verbose_name='Ссылка на 3D Модель')


    class Meta:
        ordering = ('-pk',)

    def __str__(self) -> str:
        return str(self.name)


# Исследование
class Task(models.Model):
    type = models.IntegerField(verbose_name='Тип работы')
    result = models.CharField(max_length=200, verbose_name='Результат', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.result)


# Список исследований
class LabObject(models.Model):
    object = models.ForeignKey(
        Object,
        related_name='lab_object',
        verbose_name='Объект',
        on_delete=models.CASCADE
    )
    laboratory = models.ForeignKey(
        Lab,
        related_name='lab_object',
        verbose_name='Лаборатория',
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(verbose_name='Время старта работы')
    end_date = models.DateTimeField(auto_now_add=True, verbose_name='Время конца работы')
    author = models.ForeignKey(
        User,
        related_name='lab_object',
        verbose_name='Оператор',
        on_delete=models.CASCADE,  
        default = 1
    )
    task = models.ForeignKey(
        Task,
        related_name='lab_object',
        verbose_name='Исследование',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self) -> str:
        return (str(self.object.name) + ':' + str(self.laboratory.name))
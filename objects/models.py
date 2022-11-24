from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Object(models.Model):
    name = models.IntegerField(verbose_name='Номер объекта')
    field = models.IntegerField(verbose_name='Номер месторождения')
    income_date = models.DateTimeField(auto_now_add=True, verbose_name='Время получения')

    def __str__(self) -> str:
        return str(self.name)
    

class Lab(models.Model):
    name = models.IntegerField(verbose_name='Номер лаборатории')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Время старта работы')
    end_date = models.DateTimeField(auto_now_add=True, verbose_name='Время конца работы')
    author = models.ForeignKey(
        User,
        related_name='lab',
        verbose_name='Оператор',
        on_delete=models.CASCADE,
        default = 1
    )

    task = models.IntegerField(verbose_name='Номер работы')

    def __str__(self) -> str:
        return str(self.name)


class LabObject(models.Model):
    object = models.ForeignKey(
        Object,
        related_name='lab',
        verbose_name='Логи объекта',
        on_delete=models.CASCADE
        
    )
    laboratory = models.ForeignKey(
        Lab,
        related_name='lab',
        verbose_name='Логи лаборатории',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return (str(self.object.name) + ':' + str(self.laboratory.name))


class Field(models.Model):
    field_well = models.ForeignKey(
        Object,
        related_name='oilfield', ##
        verbose_name='Родительское месторождение',
        on_delete=models.CASCADE,
        default=0
    )
    name = models.CharField(max_length=200, verbose_name='Название скважины')

    def __str__(self) -> str:
        return str(self.name)

    
class Well(models.Model):
    well_layer = models.ForeignKey(
        Field,
        related_name='oilfield', ##
        verbose_name='Родиетельская скважина',
        on_delete=models.CASCADE,
        default=0
    )
    name = models.CharField(max_length=200, verbose_name='Название пласта')

    def __str__(self) -> str:
        return str(self.name)
    

class Layer(models.Model):
    layer = models.ForeignKey(
        Well,
        related_name='oilfield',
        verbose_name='Пласт',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, verbose_name='Название пласта')

    def __str__(self) -> str:
        return str(self.name)


class Task(models.Model):
    task_lab = models.ForeignKey(
        Lab,
        related_name='taskforlab',
        verbose_name='Lab',
        on_delete=models.CASCADE
    )
    type = models.IntegerField(verbose_name='Тип работы')
    result = models.CharField(max_length=200, verbose_name='Результат работы')

    def __str__(self) -> str:
        return str(self.result)

    
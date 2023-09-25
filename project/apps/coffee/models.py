from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.constraints import CheckConstraint

from apps.coffee.coffee_enums import GrindEnums, TemperatureEnums, RateEnums


class Beans(models.Model):
    """Тип зерна."""
    title = models.CharField(verbose_name="Название типа зерна", max_length=254)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тип зерна'
        verbose_name_plural = 'Типы зерна'


class Brew(models.Model):
    """Вариант заварки."""
    beans = models.ForeignKey(Beans, verbose_name="Тип зерна", on_delete=models.PROTECT)
    grind = models.IntegerField(verbose_name="Помол", default=GrindEnums.DEFAULT_GRIND.value,
                                    validators=[
                                        MinValueValidator(GrindEnums.MIN_GRIND.value),
                                        MaxValueValidator(GrindEnums.MAX_GRIND.value)
                                    ])
    bean_weight = models.IntegerField(verbose_name="Вес зерен")
    water_weight = models.IntegerField(verbose_name="Вес воды")
    temperature = models.FloatField(verbose_name="Температура воды", blank=True, null=True,
                                    validators=[
                                        MinValueValidator(TemperatureEnums.MIN_TEMPERATURE.value),
                                        MaxValueValidator(TemperatureEnums.MAX_TEMPERATURE.value)])
    rate = models.IntegerField(verbose_name="Оценка",
                                    validators=[
                                        MinValueValidator(RateEnums.MIN_RATE.value),
                                        MaxValueValidator(RateEnums.MAX_RATE.value)])
    notes = models.TextField(verbose_name='Заметки', blank=True)

    class Meta:
        verbose_name = 'Заварка'
        verbose_name_plural = 'Варианты заварок'
        constraints = (
            CheckConstraint(
                check=models.Q(temperature__isnull=True) |
                      (
                              models.Q(temperature__gte=TemperatureEnums.MIN_TEMPERATURE.value) &
                              models.Q(temperature__lte=TemperatureEnums.MAX_TEMPERATURE.value)
                      ),
                name='temperature_range'),
            CheckConstraint(
                check=models.Q(grind__gte=GrindEnums.MIN_GRIND.value) & models.Q(grind__lte=GrindEnums.MAX_GRIND.value),
                name='grind_range'),
            CheckConstraint(
                check=models.Q(rate__gte=RateEnums.MIN_RATE.value) & models.Q(rate__lte=RateEnums.MAX_RATE.value),
                name='rate_range')
        )

    def __str__(self):
        return f'{self.beans.title}'

from django import forms
from django.contrib import admin
from django.forms.widgets import NumberInput

from rangefilter.filters import NumericRangeFilter

from apps.coffee.coffee_enums import GrindEnums, TemperatureEnums, RateEnums
from apps.coffee.models import Beans, Brew


class RangeInput(NumberInput):
    input_type = 'range'
    template_name = 'admin/range_input.html'


class BrewForm(forms.ModelForm):

    class Meta:
        model = Brew
        fields = '__all__'
        widgets = {
            'grind': RangeInput(attrs={'max': GrindEnums.MAX_GRIND.value, 'min': GrindEnums.MIN_GRIND.value,
                                       'oninput': 'this.nextElementSibling.textContent=this.value'}),
            'temperature': NumberInput(attrs={'max': TemperatureEnums.MAX_TEMPERATURE.value,
                                              'min': TemperatureEnums.MIN_TEMPERATURE.value}),
            'rate': NumberInput(attrs={'max': RateEnums.MAX_RATE.value, 'min': RateEnums.MIN_RATE.value}),
        }


class BrewAdmin(admin.ModelAdmin):
    model = Brew
    form = BrewForm

    search_fields = ['beans__title']
    list_filter = ['beans', ("temperature", admin.EmptyFieldListFilter), ("notes", admin.EmptyFieldListFilter),
                   ("rate", NumericRangeFilter)]
    list_display = ['beans', 'grind', 'bean_weight', 'water_weight', 'temperature', 'rate']


admin.site.register(Beans, admin.ModelAdmin)
admin.site.register(Brew, BrewAdmin)

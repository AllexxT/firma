from django.contrib import admin
from .models import Sklad, Trotuarka, Zabor, Materials, ColorAndPrice

# Register your models here.


@admin.register(ColorAndPrice)
class ColorAndPriceAdmin(admin.ModelAdmin):
    fields = (
        'cost',
        'color',
        'amount',
        'trotuarka'
    )
    list_display = (
        'showName',
        'color',
        'cost',
        'amount'
    )


@admin.register(Sklad)
class SkladAdmin(admin.ModelAdmin):

    class ZaborInline(admin.StackedInline):
        model = Zabor
        extra = 0
    class TrotuarkaInline(admin.StackedInline):
        model = Trotuarka
        extra = 0
    
    inlines = [ZaborInline, TrotuarkaInline]
    
    fields = (
        'storage',
    )

    # list_display = (
    #     'storage',
    # )


@admin.register(Trotuarka)
class TrotuarkaAdmin(admin.ModelAdmin):

    class ColorAndPriceInline(admin.TabularInline):
        model = ColorAndPrice
        extra = 0
    inlines = [ColorAndPriceInline,]

    fields = (
        'name',
        'sklad',
        'description',
    )

    list_display = (
        'name',
        'sklad',
        'description',
        'amount',
    )

@admin.register(Zabor)
class ZaborkAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'sklad',
        'price',
        'description',
        'amount',
    )

    list_display = (
        'name',
        'sklad',
        'price',
        'description',
        'amount',
    )

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    fields = (
        'sklad',
        'pesok',
        'cement',
        'scheben',
        'zavoz',
    )

    list_display = (
        'sklad',
        'pesok',
        'cement',
        'scheben',
        'zavoz',
    )

from django.contrib import admin
from .models import Sklad, Trotuarka, Zabor, Materials

# Register your models here.



@admin.register(Sklad)
class SkladAdmin(admin.ModelAdmin):

    class ZaborInline(admin.StackedInline):
        model = Zabor
        extra = 0
    class TrotuarkaInline(admin.StackedInline):
        model = Trotuarka
        extra = 2
    
    inlines = [ZaborInline, TrotuarkaInline]
    
    fields = (
        'storage',
    )

    # list_display = (
    #     'storage',
    # )


@admin.register(Trotuarka)
class TrotuarkaAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'sklad',
        'price',
        'description',
        'color',
        'amount',
    )

    list_display = (
        'name',
        'sklad',
        'price',
        'description',
        'color',
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

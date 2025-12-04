from django.contrib import admin
from .models import Cargo, CargoHistory, Ticket

class CargoHistoryInline(admin.TabularInline):
    model = CargoHistory
    extra = 1 
    readonly_fields = ('tarih',)
    fields = ('konum', 'detay') 

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'takip_no', 
        'alici', 
        'durum', 
        'fiyat', 
        'olusturma'
    )
    list_filter = ('durum',)
    search_fields = ('takip_no', 'alici')
    readonly_fields = ('olusturma', 'guncelleme')
    inlines = [CargoHistoryInline]

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Ticket Yönetimi Listesi
    list_display = ('id', 'konu', 'email', 'durum', 'olusturma')
    list_filter = ('durum', 'konu')
    search_fields = ('email', 'mesaj')
    readonly_fields = ('olusturma', 'guncelleme')
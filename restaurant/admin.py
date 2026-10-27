from django.contrib import admin
from .models import Booking, Menu


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    list_filter = ('booking_date',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    search_fields = ('title',)
    list_filter = ('price',)

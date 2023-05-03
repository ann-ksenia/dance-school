from django.contrib import admin
from django.contrib import messages
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user',)
    list_display_links = ('id','user',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone',)
    list_display_links = ('id','name',)

class Style_descriptionAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'teacher',)
    list_display_links = ('id','title',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount','price',)
    list_display_links = ('id', 'amount',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Style_description, Style_descriptionAdmin)
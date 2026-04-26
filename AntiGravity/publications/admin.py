from django.contrib import admin
from .models import Faculty, Publication

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'joining_date')
    search_fields = ('name', 'designation')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty', 'pub_type', 'year')
    list_filter = ('pub_type', 'year', 'month')
    search_fields = ('title', 'venue_name', 'faculty__name')

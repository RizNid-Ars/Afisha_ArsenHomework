from django.contrib import admin
from .models import Director, Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')
    list_filter = ('director',)
    search_fields = ('title', 'director__name')



admin.site.register(Director)
admin.site.register(Review)



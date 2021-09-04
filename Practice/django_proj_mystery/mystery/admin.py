from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from mystery.models import Ufo, Creature, Timetravel, Video, Review


@admin.register(Ufo)
class UfoAdmin(admin.ModelAdmin):
    sarch_fields = (Ufo)
    list_display = ['case', 'photo', 'time', 'area', 'desc', 'created_at']


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    sarch_fields = (Creature)
    list_display = ['case', 'photo', 'time', 'area', 'desc', 'created_at']


@admin.register(Timetravel)
class TimetravelAdmin(admin.ModelAdmin):
    sarch_fields = (Timetravel)
    list_display = ['case', 'photo', 'time', 'area', 'desc', 'created_at']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'youtube_url', 'created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

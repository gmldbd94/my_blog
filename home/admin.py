from django.contrib import admin
from . import models
#
# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Lecture)
class LectureAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


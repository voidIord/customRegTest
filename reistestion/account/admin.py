from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import Group


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)


admin.site.register(GroupNames)
admin.site.register(SubjectsNames)
admin.site.register(ModulesNames)
admin.site.register(ThemesNames)
admin.site.register(TasksNames)
admin.site.register(LessonsNames)
admin.site.register(ViewSubjectTopics)
admin.site.register(GroupsSubjects)
admin.site.register(SubjectsTeachers)
admin.site.register(SubjectsModules)
admin.site.register(ModuleThemes)
admin.site.register(ThemesLessons)
admin.site.register(LessonsTasks)
admin.site.register(TasksStudents)
admin.site.register(Semester)
admin.site.register(SemestersSubjects)
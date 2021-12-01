# Generated by Django 3.2.2 on 2021-11-21 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20211121_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonsnames',
            name='theme',
            field=models.ManyToManyField(blank=True, through='account.ThemesLessons', to='account.ThemesNames'),
        ),
        migrations.AddField(
            model_name='modulesnames',
            name='theme',
            field=models.ManyToManyField(blank=True, through='account.ModuleThemes', to='account.ThemesNames'),
        ),
        migrations.AddField(
            model_name='subjectsnames',
            name='group',
            field=models.ManyToManyField(blank=True, through='account.GroupsSubjects', to='account.GroupNames'),
        ),
        migrations.AddField(
            model_name='subjectsnames',
            name='teacher',
            field=models.ManyToManyField(blank=True, through='account.SubjectsTeachers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasksnames',
            name='lesson',
            field=models.ManyToManyField(blank=True, through='account.LessonsTasks', to='account.LessonsNames'),
        ),
        migrations.AddField(
            model_name='tasksnames',
            name='student',
            field=models.ManyToManyField(blank=True, through='account.TasksStudents', to=settings.AUTH_USER_MODEL),
        ),
    ]
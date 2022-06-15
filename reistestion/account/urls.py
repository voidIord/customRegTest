from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('account/', profile, name='account'),
    path('disciplines/', disciplines, name='disciplines'),
    path('disciplines/<int:pk>', view_disciplines.as_view(), name='view-disciplines'),
    path('management/', management, name='management'),
    path('management/groups/', show_groups, name='groups'),
    path('alerts/', alerts, name='alerts'),
    path('profile/', account_view, name='profile'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('display_table/', displaing_table_of_subjects, name='display-table'),
    path('management/groups/<int:pk>', dinamic.as_view(), name='group-detail'),
    path('display_table/<int:pk>/', displaing_table.as_view(), name='display-one-table'),
    path('table/', table_view, name='TableForSemester'),
    path('table_of_subject/', displaing_table_of_subjects, name='TableForSubjects')
]

urlpatterns += [
    path('group/', group, name='group'),
    path('<int:pk>/update', update.as_view(), name='group-update'),
    path('<int:pk>/delete', delete.as_view(), name='group-delete'),

    path('image/', image_view, name='image'),
    path('display_table/addtable/', table_view, name='TableForSemester'),
    path('table_of_subject/', displaing_table_of_subjects, name='TableForSubjects'),
    path('interface/', interface, name='interface'),

    path('subjects/', subjects_names_view, name='TableForSubjects'),
    path('subjects-groups/', groups_subjects_view, name='TableForSubjectsNames'),
    path('subjects-teachers/', subjects_teachers_view, name='TableForSubjectsTeachers'),
    path('semesters-subjects/', semesters_subjects_view, name='TableForSemestersSubjects'),
    path('themes-names/', themes_names_view, name='TableForThemesNames'),
    path('modules-names/', modules_names_view, name='TableForModulesNames'),
    path('subjects-modules/', subjects_modules_view, name='TableForSubjectsModules'),
    path('lessons-names/', lessons_names_view, name='TableForLessonsNames'),
    path('tasks-names/', tasks_names_view, name='TableForTasksNames'),
    path('modules-themes/', modules_themes_view, name='TableForModuleThemes'),
    path('themes-lessons/', themes_lessons_view, name='TableForThemesLessons'),
    path('lessons-tasks/', lessons_tasks_view, name='TableForLessonsTasks'),
    path('tasks-students/', tasks_students_view, name='TableForTasksStudents'),
    path('navigation/', navigate, name='NavigateForTables'),
    path('changepass/', password_change, name='changepwd')
]

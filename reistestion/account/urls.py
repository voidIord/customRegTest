from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_view, name='home'),
    path('group', views.group, name='group'),
    path('<int:pk>', views.dinamic.as_view(), name='group-detail'),
    path('<int:pk>/update', views.update.as_view(), name='group-update'),
    path('<int:pk>/delete', views.delete.as_view(), name='group-delete'),


    path('display_table', views.displaing_table_of_subjects, name='display-table'),
    path('<int:pk>/display_one_table', views.displaing_table.as_view(), name='display-one-table'),

    path('account/', views.profile, name='profile'),
    path('register/', views.registration_view, name='register'),
    path('image/', views.image_view, name='image'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('table/', views.table_view, name='TableForSemester'),
    path('table_of_subject/', views.displaing_table_of_subjects, name='TableForSubjects'),
    path('interface/', views.interface, name='interface'),

    path('subjects/', views.subjects_names_view, name='TableForSubjects'),
    path('subjects-groups/', views.groups_subjects_view, name='TableForSubjectsNames'),
    path('subjects-teachers/', views.subjects_teachers_view, name='TableForSubjectsTeachers'),
    path('semesters-subjects/', views.semesters_subjects_view, name='TableForSemestersSubjects'),
    path('themes-names/', views.themes_names_view, name='TableForThemesNames'),
    path('modules-names/', views.modules_names_view, name='TableForModulesNames'),
    path('subjects-modules/', views.subjects_modules_view, name='TableForSubjectsModules'),
    path('lessons-names/', views.lessons_names_view, name='TableForLessonsNames'),
    path('tasks-names/', views.tasks_names_view, name='TableForTasksNames'),
    path('modules-themes/', views.modules_themes_view, name='TableForModuleThemes'),
    path('themes-lessons/', views.themes_lessons_view, name='TableForThemesLessons'),
    path('lessons-tasks/', views.lessons_tasks_view, name='TableForLessonsTasks'),
    path('tasks-students/', views.tasks_students_view, name='TableForTasksStudents'),
    path('navigation/', views.navigate, name='NavigateForTables'),
    path('changepass/', views.password_change, name='changepwd')
]

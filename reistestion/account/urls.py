from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface, name='interface'),
    path('group', views.group, name='group'),
    path('<int:pk>', views.dinamic.as_view(), name='group-detail'),
    path('<int:pk>/update', views.update.as_view(), name='group-update'),
    path('<int:pk>/delete', views.delete.as_view(), name='group-delete'),

    path('register/', views.registration_view, name='register'),
    path('image/', views.image_view, name='image'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('table/', views.table_view, name='TableForSemester'),

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
]

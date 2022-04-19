from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import GroupNames, SemestersSubjects, SubjectsTeachers, ThemesNames, ModulesNames, SubjectsModules, \
    LessonsNames, TasksNames, ModuleThemes, ThemesLessons, LessonsTasks, TasksStudents, GroupsSubjects, SubjectsNames
from django.forms import ModelForm, TextInput

from .models import Account, Semester


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Неверный пароль")


class ImageForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('prof_img',)

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        return gender

    def clean_phone_no(self):
        phone_no = self.cleaned_data['phone_no']
        return phone_no

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img


class GroupForm(ModelForm):
    class Meta:
        model = GroupNames
        fields = ['GroupName']

        widgets = \
        {
            "GroupName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Группы',
            }),
        }


class TableUpdateForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('Sem', 'Week1_1','Week2_1','Week3_1','Week4_1','Week5_1','Week6_1','Week7_1','Week8_1','Week9_1',
                  'Week10_1','Week11_1','Week12_1','Week13_1','Week14_1','Week15_1','Week16_1','Week17_1','Week18_1',
                  'Week1_2','Week2_2','Week3_2','Week4_2','Week5_2','Week6_2','Week7_2','Week8_2','Week9_2',
                  'Week10_2','Week11_2','Week12_2','Week13_2','Week14_2','Week15_2','Week16_2','Week17_2','Week18_2',
                  'Week1_3','Week2_3','Week3_3','Week4_3','Week5_3','Week6_3','Week7_3','Week8_3','Week9_3',
                  'Week10_3','Week11_3','Week12_3','Week13_3','Week14_3','Week15_3','Week16_3','Week17_3','Week18_3',
                  'Week1_4','Week2_4','Week3_4','Week4_4','Week5_4','Week6_4','Week7_4','Week8_4','Week9_4',
                  'Week10_4','Week11_4','Week12_4','Week13_4','Week14_4','Week15_4','Week16_4','Week17_4','Week18_4',
                  'Week1_5','Week2_5','Week3_5','Week4_5','Week5_5','Week6_5','Week7_5','Week8_5','Week9_5',
                  'Week10_5','Week11_5','Week12_5','Week13_5','Week14_5','Week15_5','Week16_5','Week17_5','Week18_5',
                  'Week1_6','Week2_6','Week3_6','Week4_6','Week5_6','Week6_6','Week7_6','Week8_6','Week9_6',
                  'Week10_6','Week11_6','Week12_6','Week13_6','Week14_6','Week15_6','Week16_6','Week17_6','Week18_6')

    widgets = \
        {
            "Sem": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер семестра',
            }),

            "Week1_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание1',
            }),

            "Week2_1": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Неделя 2_задание1',
            }),

        "Week3_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание1',
        }),

        "Week4_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание1',
        }),

        "Week5_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание1',
        }),

        "Week6_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание1',
        }),

        "Week7_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание1',
        }),

        "Week8_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание1',
        }),

        "Week9_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание1',
        }),

        "Week10_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание1',
        }),

        "Week11_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание1',
        }),

        "Week12_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание1',
        }),

        "Week13_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание1',
        }),

        "Week14_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание1',
        }),

        "Week15_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание1',
        }),

        "Week16_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание1',
        }),

        "Week17_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание1',
        }),

        "Week18_1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание1',
        }),

        "Week1_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание2',
        }),

        "Week2_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2_задание2',
        }),

        "Week3_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание2',
        }),

        "Week4_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание2',
        }),

        "Week5_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание2',
        }),

        "Week6_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание2',
        }),

        "Week7_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание2',
        }),

        "Week8_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание2',
        }),

        "Week9_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание2',
        }),

        "Week10_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание2',
        }),

        "Week11_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание2',
        }),

        "Week12_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание2',
        }),

        "Week13_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание2',
        }),

        "Week14_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание2',
        }),

        "Week15_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание2',
        }),

        "Week16_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание2',
        }),

        "Week17_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание2',
        }),

        "Week18_2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание2',
        }),

        "Week1_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание3',
        }),

        "Week2_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2_задание3',
        }),

        "Week3_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание3',
        }),

        "Week4_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание3',
        }),

        "Week5_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание3',
        }),

        "Week6_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание3',
        }),

        "Week7_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание3',
        }),

        "Week8_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание3',
        }),

        "Week9_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание3',
        }),

        "Week10_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание3',
        }),

        "Week11_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание3',
        }),

        "Week12_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание3',
        }),

        "Week13_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание3',
        }),

        "Week14_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание3',
        }),

        "Week15_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание3',
        }),

        "Week16_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание3',
        }),

        "Week17_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание3',
        }),

        "Week18_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание3',
        }),

        "Week1_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание4',
        }),

        "Week2_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2_задание4',
        }),

        "Week3_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание4',
        }),

        "Week4_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание4',
        }),

        "Week5_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание4',
        }),

        "Week6_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание4',
        }),

        "Week7_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание4',
        }),

        "Week8_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание4',
        }),

        "Week9_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание4',
        }),

        "Week10_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание4',
        }),

        "Week11_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание4',
        }),

        "Week12_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание4',
        }),

        "Week13_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание4',
        }),

        "Week14_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание4',
        }),

        "Week15_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание4',
        }),

        "Week16_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание4',
        }),

        "Week17_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание4',
        }),

        "Week18_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание4',
        }),

        "Week1_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание5',
        }),

        "Week2_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2_задание5',
        }),

        "Week3_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание5',
        }),

        "Week4_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание5',
        }),

        "Week5_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание5',
        }),

        "Week6_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание5',
        }),

        "Week7_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание5',
        }),

        "Week8_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание5',
        }),

        "Week9_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание5',
        }),

        "Week10_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание5',
        }),

        "Week11_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание5',
        }),

        "Week12_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание5',
        }),

        "Week13_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание5',
        }),

        "Week14_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание5',
        }),

        "Week15_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание5',
        }),

        "Week16_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание5',
        }),

        "Week17_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание5',
        }),

        "Week18_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание5',
        }),

        "Week1_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1_задание6',
        }),

        "Week2_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2_задание6',
        }),

        "Week3_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3_задание6',
        }),

        "Week4_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4_задание6',
        }),

        "Week5_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5_задание6',
        }),

        "Week6_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6_задание6',
        }),

        "Week7_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7_задание6',
        }),

        "Week8_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8_задание6',
        }),

        "Week9_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9_задание6',
        }),

        "Week10_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10_задание6',
        }),

        "Week11_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11_задание6',
        }),

        "Week12_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12_задание6',
        }),

        "Week13_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13_задание6',
        }),

        "Week14_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14_задание6',
        }),

        "Week15_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15_задание6',
        }),

        "Week16_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16_задание6',
        }),

        "Week17_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 17_задание6',
        }),

        "Week18_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 18_задание6',
        }),
    }


class SubjectsNamesForm(ModelForm):
    class Meta:
        model = SubjectsNames
        fields = ['SubjectName', 'group', 'teacher']

        widgets = \
        {
            "SubjectName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета',
            }),

            "group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название группы',
            }),

            "teacher": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО преподавателя',
            }),
        }


class GroupsSubjectsForm(ModelForm):
    class Meta:
        model = GroupsSubjects
        fields = ['Group', 'Subject']

        widgets = \
        {
            "Group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название группы',
            }),

            "Subject": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета',
            }),
        }


class SubjectsTeachersForm(ModelForm):
    class Meta:
        model = SubjectsTeachers
        fields = ['Subject', 'Teacher']

        widgets = \
        {
            "Subject": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета',
            }),

            "Teacher": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО преподавателя',
            }),

        }


class SemestersSubjectsForm(ModelForm):
    class Meta:
        model = SemestersSubjects
        fields = ['semester', 'subject']

        widgets = \
        {
            "semester": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер семестра',
            }),

            "subject": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета',
            }),

        }


class ThemesNamesForm(ModelForm):
    class Meta:
        model = ThemesNames
        fields = ['ThemeName']

        widgets = \
        {
            "ThemeName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название темы',
            }),

        }


class ModulesNamesForm(ModelForm):
    class Meta:
        model = ModulesNames
        fields = ['ModelName', 'subjects', 'theme']

        widgets = \
        {
            "ModelName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название модуля',
            }),

            "subjects": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета',
            }),

            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема',
            }),
        }


class SubjectsModulesForm(ModelForm):
    class Meta:
        model = SubjectsModules
        fields = ['Subject', 'Module']

        widgets = \
        {
            "Subject": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет',
            }),

            "Module": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модуль',
            }),

        }


class LessonsNamesForm(ModelForm):
    class Meta:
        model = LessonsNames
        fields = ['LessonName', 'TaskName', 'theme']

        widgets = \
        {
            "LessonName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время проведения пары',
            }),

            "TaskName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер пары',
            }),

            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема',
            }),
        }


class TasksNamesForm(ModelForm):
    class Meta:
        model = TasksNames
        fields = ['TaskName', 'TaskDescription', 'TaskMark', 'student', 'lesson']

        widgets = \
        {
            "TaskName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задания',
            }),

            "TaskDescription": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задания',
            }),

            "TaskMark": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимальный балл за задание',
            }),

            "student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО студента',
            }),

            "lesson": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пара',
            }),
        }


class ModuleThemesForm(ModelForm):
    class Meta:
        model = ModuleThemes
        fields = ['Model', 'Theme']

        widgets = \
        {
            "Model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название модуля',
            }),

            "Theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название темы',
            }),

        }


class ThemesLessonsForm(ModelForm):
    class Meta:
        model = ThemesLessons
        fields = ['Theme', 'Lesson']

        widgets = \
        {
            "Theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название темы',
            }),

            "Lesson": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пара',
            }),

        }


class LessonsTasksForm(ModelForm):
    class Meta:
        model = LessonsTasks
        fields = ['Lesson', 'Task']

        widgets = \
        {
            "Lesson": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пара',
            }),

            "Task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание',
            }),

        }


class TasksStudentsForm(ModelForm):
    class Meta:
        model = TasksStudents
        fields = ['Task', 'Student', 'Mark']

        widgets = \
        {
            "Task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задание',
            }),

            "Student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО студента',
            }),

            "Mark": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка',
            }),
        }
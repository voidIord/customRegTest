from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, gender, phone_no, prof_img, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            gender=gender,
            phone_no=phone_no,
            prof_img=prof_img,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            gender=None,
            phone_no=None,
            prof_img=None,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=False)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    prof_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True,
                                 blank=True)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_teacher = models.BooleanField(default=False)
    first_name = models.TextField(verbose_name='name', max_length=32)
    last_name = models.TextField(verbose_name='surname', max_length=32)
    group = models.ForeignKey("GroupNames", on_delete=models.PROTECT, null=True, verbose_name='group_key')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


    def get_absolut_url(self):
        return f'/qnew/{self.id}'

    class Meta:
        verbose_name = 'Аккаунты'
        verbose_name_plural = 'Аккаунты'


class GroupNames(models.Model):
    GroupName = models.CharField('Название Группы', max_length=10)


    def __str__(self):
        return self.GroupName

    def get_absolut_url(self):
        return f'/gnew/{self.id}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class SubjectsNames(models.Model):
    SubjectName = models.CharField('Название дисциплины', max_length=64)
    group = models.ManyToManyField(GroupNames, blank=True, through='GroupsSubjects')
    teacher = models.ManyToManyField(Account, blank=True, through='SubjectsTeachers')

    def __str__(self):
        return self.SubjectName

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class GroupsSubjects(models.Model):
    Group = models.ForeignKey("GroupNames", on_delete=models.CASCADE, null=True, verbose_name='Group_key')
    Subject = models.ForeignKey("SubjectsNames", on_delete=models.CASCADE, null=True, verbose_name='Subject_key')

    def __int__(self):
        return self.Subject

    class Meta:
        verbose_name = 'Связь: Предмет - Группа'
        verbose_name_plural = 'Связь: Предмет - Группа'


class SubjectsTeachers(models.Model):
    Subject = models.ForeignKey("SubjectsNames", on_delete=models.CASCADE, null=True, verbose_name='Subject_key')
    Teacher = models.ForeignKey("Account", on_delete=models.CASCADE, null=True, verbose_name='Teacher_key')

    def __int__(self):
        return self.Teacher

    class Meta:
        verbose_name = 'Связь: Предмет - Педагог'
        verbose_name_plural = 'Связь: Предмет - Педагог'


class Semester(models.Model):
    Sem = models.IntegerField('Номер семестра', null=False, unique=False)
    Week1 = models.CharField('Неделя 1', max_length=255, blank=True, unique=False)
    Week2 = models.CharField('Неделя 2', max_length=255, blank=True, unique=False)
    Week3 = models.CharField('Неделя 3', max_length=255, blank=True, unique=False)
    Week4 = models.CharField('Неделя 4', max_length=255, blank=True, unique=False)
    Week5 = models.CharField('Неделя 5', max_length=255, blank=True, unique=False)
    Week6 = models.CharField('Неделя 6', max_length=255, blank=True, unique=False)
    Week7 = models.CharField('Неделя 7', max_length=255, blank=True, unique=False)
    Week8 = models.CharField('Неделя 8', max_length=255, blank=True, unique=False)
    Week9 = models.CharField('Неделя 9', max_length=255, blank=True, unique=False)
    Week10 = models.CharField('Неделя 10', max_length=255, blank=True, unique=False)
    Week11 = models.CharField('Неделя 11', max_length=255, blank=True, unique=False)
    Week12 = models.CharField('Неделя 12', max_length=255, blank=True, unique=False)
    Week13 = models.CharField('Неделя 13', max_length=255, blank=True, unique=False)
    Week14 = models.CharField('Неделя 14', max_length=255, blank=True, unique=False)
    Week15 = models.CharField('Неделя 15', max_length=255, blank=True, unique=False)
    Week16 = models.CharField('Неделя 16', max_length=255, blank=True, unique=False)
    subjects = models.ManyToManyField(SubjectsNames, blank=True, through='SemestersSubjects')

    def __int__(self):
        return self.Sem

    def get_absolut_url(self):
        return f'/qnew/{self.id}'

    class Meta:
        verbose_name = 'Семестры'
        verbose_name_plural = 'Семестры'


class SemestersSubjects(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsNames, on_delete=models.CASCADE)

    def __int__(self):
        return self.semester, self.subject

    class Meta:
        verbose_name = 'Связь: Предмет - Семестр'
        verbose_name_plural = 'Связь: Предмет - Семестр'


class ThemesNames(models.Model):
    ThemeName = models.CharField('Название темы', max_length=64)

    def __str__(self):
        return self.ThemeName

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class ModulesNames(models.Model):
    ModelName = models.CharField('Название модуля', max_length=64)
    subjects = models.ManyToManyField(SubjectsNames, blank=True, through='SubjectsModules')
    theme = models.ManyToManyField(ThemesNames, blank=True, through='ModuleThemes')

    def __str__(self):
        return self.ModelName

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'


class SubjectsModules(models.Model):
    Subject = models.ForeignKey(SubjectsNames, on_delete=models.CASCADE)
    Module = models.ForeignKey(ModulesNames, on_delete=models.CASCADE)

    def __int__(self):
        return self.Module

    class Meta:
        verbose_name = 'Связь: Предмет - Модуль'
        verbose_name_plural = 'Связь: Предмет - Модуль'


class LessonsNames(models.Model):
    LessonName = models.DateTimeField('Дата и время проведения пары')
    TaskName = models.IntegerField('Номер пары')
    theme = models.ManyToManyField(ThemesNames, blank=True, through='ThemesLessons')

    def __int__(self):
        return self.TaskName

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class TasksNames(models.Model):
    TaskName = models.CharField('Название задания', max_length=64)
    TaskDescription = models.TextField('Описание задания', max_length=1024)
    TaskMark = models.IntegerField('Максимальный балл за задание')
    student = models.ManyToManyField(Account, blank=True, through='TasksStudents')
    lesson = models.ManyToManyField(LessonsNames, blank=True, through='LessonsTasks')

    def __str__(self):
        return self.TaskName

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Заданния'


class ModuleThemes(models.Model):
    Model = models.ForeignKey("ModulesNames", on_delete=models.CASCADE, null=True, verbose_name='Module_key')
    Theme = models.ForeignKey("ThemesNames", on_delete=models.CASCADE, null=True, verbose_name='Theme_key')

    def __int__(self):
        return self.Theme

    class Meta:
        verbose_name = 'Связь: Тема - Модуль'
        verbose_name_plural = 'Связь: Тема - Модуль'


class ThemesLessons(models.Model):
    Theme = models.ForeignKey("ThemesNames", on_delete=models.CASCADE, null=True, verbose_name='Theme_key')
    Lesson = models.ForeignKey("LessonsNames", on_delete=models.CASCADE, null=True, verbose_name='Lessons_key')

    def __int__(self):
        return self.Lesson

    class Meta:
        verbose_name = 'Связь: Тема - Занятие'
        verbose_name_plural = 'Связь: Тема - Занятие'


class LessonsTasks(models.Model):
    Lesson = models.ForeignKey("LessonsNames", on_delete=models.CASCADE, null=True, verbose_name='Lessons_key')
    Task = models.ForeignKey("TasksNames", on_delete=models.CASCADE, null=True, verbose_name='Task_key')

    def __int__(self):
        return self.Task

    class Meta:
        verbose_name = 'Связь: Тема - Задание'
        verbose_name_plural = 'Связь: Тема - Задание'


class TasksStudents(models.Model):
    Task = models.ForeignKey("TasksNames", on_delete=models.CASCADE, null=True, verbose_name='Task_key')
    Student = models.ForeignKey("Account", on_delete=models.CASCADE, null=True, verbose_name='Students_key')
    Mark = models.IntegerField("Оценка")

    def __int__(self):
        return self.Mark

    class Meta:
        verbose_name = 'Связь: Студент - Задание'
        verbose_name_plural = 'Связь: Студент - Задание'

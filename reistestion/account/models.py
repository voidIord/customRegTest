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
    Week1_1 = models.CharField('Неделя1_задание1', max_length=255, blank=True, unique=False)
    Week2_1 = models.CharField('Неделя2_задание1', max_length=255, blank=True, unique=False)
    Week3_1 = models.CharField('Неделя3_задание1', max_length=255, blank=True, unique=False)
    Week4_1 = models.CharField('Неделя4_задание1', max_length=255, blank=True, unique=False)
    Week5_1 = models.CharField('Неделя5_задание1', max_length=255, blank=True, unique=False)
    Week6_1 = models.CharField('Неделя6_задание1', max_length=255, blank=True, unique=False)
    Week7_1 = models.CharField('Неделя7_задание1', max_length=255, blank=True, unique=False)
    Week8_1 = models.CharField('Неделя8_задание1', max_length=255, blank=True, unique=False)
    Week9_1 = models.CharField('Неделя9_задание1', max_length=255, blank=True, unique=False)
    Week10_1 = models.CharField('Неделя10_задание1', max_length=255, blank=True, unique=False)
    Week11_1 = models.CharField('Неделя11_задание1', max_length=255, blank=True, unique=False)
    Week12_1 = models.CharField('Неделя12_задание1', max_length=255, blank=True, unique=False)
    Week13_1 = models.CharField('Неделя13_задание1', max_length=255, blank=True, unique=False)
    Week14_1 = models.CharField('Неделя14_задание1', max_length=255, blank=True, unique=False)
    Week15_1 = models.CharField('Неделя15_задание1', max_length=255, blank=True, unique=False)
    Week16_1 = models.CharField('Неделя16_задание1', max_length=255, blank=True, unique=False)
    Week17_1 = models.CharField('Неделя17_задание1', max_length=255, blank=True, unique=False)
    Week18_1 = models.CharField('Неделя18_задание1', max_length=255, blank=True, unique=False)

    Week1_2 = models.CharField('Неделя1_задание2', max_length=255, blank=True, unique=False)
    Week2_2 = models.CharField('Неделя2_задание2', max_length=255, blank=True, unique=False)
    Week3_2 = models.CharField('Неделя3_задание2', max_length=255, blank=True, unique=False)
    Week4_2 = models.CharField('Неделя4_задание2', max_length=255, blank=True, unique=False)
    Week5_2 = models.CharField('Неделя5_задание2', max_length=255, blank=True, unique=False)
    Week6_2 = models.CharField('Неделя6_задание2', max_length=255, blank=True, unique=False)
    Week7_2 = models.CharField('Неделя7_задание2', max_length=255, blank=True, unique=False)
    Week8_2 = models.CharField('Неделя8_задание2', max_length=255, blank=True, unique=False)
    Week9_2 = models.CharField('Неделя9_задание2', max_length=255, blank=True, unique=False)
    Week10_2 = models.CharField('Неделя10_задание2', max_length=255, blank=True, unique=False)
    Week11_2 = models.CharField('Неделя11_задание2', max_length=255, blank=True, unique=False)
    Week12_2 = models.CharField('Неделя12_задание2', max_length=255, blank=True, unique=False)
    Week13_2 = models.CharField('Неделя13_задание2', max_length=255, blank=True, unique=False)
    Week14_2 = models.CharField('Неделя14_задание2', max_length=255, blank=True, unique=False)
    Week15_2 = models.CharField('Неделя15_задание2', max_length=255, blank=True, unique=False)
    Week16_2 = models.CharField('Неделя16_задание2', max_length=255, blank=True, unique=False)
    Week17_2 = models.CharField('Неделя17_задание2', max_length=255, blank=True, unique=False)
    Week18_2 = models.CharField('Неделя18_задание2', max_length=255, blank=True, unique=False)

    Week1_3 = models.CharField('Неделя1_задание3', max_length=255, blank=True, unique=False)
    Week2_3 = models.CharField('Неделя2_задание3', max_length=255, blank=True, unique=False)
    Week3_3 = models.CharField('Неделя3_задание3', max_length=255, blank=True, unique=False)
    Week4_3 = models.CharField('Неделя4_задание3', max_length=255, blank=True, unique=False)
    Week5_3 = models.CharField('Неделя5_задание3', max_length=255, blank=True, unique=False)
    Week6_3 = models.CharField('Неделя6_задание3', max_length=255, blank=True, unique=False)
    Week7_3 = models.CharField('Неделя7_задание3', max_length=255, blank=True, unique=False)
    Week8_3 = models.CharField('Неделя8_задание3', max_length=255, blank=True, unique=False)
    Week9_3 = models.CharField('Неделя9_задание3', max_length=255, blank=True, unique=False)
    Week10_3 = models.CharField('Неделя10_задание3', max_length=255, blank=True, unique=False)
    Week11_3 = models.CharField('Неделя11_задание3', max_length=255, blank=True, unique=False)
    Week12_3 = models.CharField('Неделя12_задание3', max_length=255, blank=True, unique=False)
    Week13_3 = models.CharField('Неделя13_задание3', max_length=255, blank=True, unique=False)
    Week14_3 = models.CharField('Неделя14_задание3', max_length=255, blank=True, unique=False)
    Week15_3 = models.CharField('Неделя15_задание3', max_length=255, blank=True, unique=False)
    Week16_3 = models.CharField('Неделя16_задание3', max_length=255, blank=True, unique=False)
    Week17_3 = models.CharField('Неделя17_задание3', max_length=255, blank=True, unique=False)
    Week18_3 = models.CharField('Неделя18_задание3', max_length=255, blank=True, unique=False)

    Week1_4 = models.CharField('Неделя1_задание4', max_length=255, blank=True, unique=False)
    Week2_4 = models.CharField('Неделя2_задание4', max_length=255, blank=True, unique=False)
    Week3_4 = models.CharField('Неделя3_задание4', max_length=255, blank=True, unique=False)
    Week4_4 = models.CharField('Неделя4_задание4', max_length=255, blank=True, unique=False)
    Week5_4 = models.CharField('Неделя5_задание4', max_length=255, blank=True, unique=False)
    Week6_4 = models.CharField('Неделя6_задание4', max_length=255, blank=True, unique=False)
    Week7_4 = models.CharField('Неделя7_задание4', max_length=255, blank=True, unique=False)
    Week8_4 = models.CharField('Неделя8_задание4', max_length=255, blank=True, unique=False)
    Week9_4 = models.CharField('Неделя9_задание4', max_length=255, blank=True, unique=False)
    Week10_4 = models.CharField('Неделя10_задание4', max_length=255, blank=True, unique=False)
    Week11_4 = models.CharField('Неделя11_задание4', max_length=255, blank=True, unique=False)
    Week12_4 = models.CharField('Неделя12_задание4', max_length=255, blank=True, unique=False)
    Week13_4 = models.CharField('Неделя13_задание4', max_length=255, blank=True, unique=False)
    Week14_4 = models.CharField('Неделя14_задание4', max_length=255, blank=True, unique=False)
    Week15_4 = models.CharField('Неделя15_задание4', max_length=255, blank=True, unique=False)
    Week16_4 = models.CharField('Неделя16_задание4', max_length=255, blank=True, unique=False)
    Week17_4 = models.CharField('Неделя17_задание4', max_length=255, blank=True, unique=False)
    Week18_4 = models.CharField('Неделя18_задание4', max_length=255, blank=True, unique=False)

    Week1_5 = models.CharField('Неделя1_задание5', max_length=255, blank=True, unique=False)
    Week2_5 = models.CharField('Неделя2_задание5', max_length=255, blank=True, unique=False)
    Week3_5 = models.CharField('Неделя3_задание5', max_length=255, blank=True, unique=False)
    Week4_5 = models.CharField('Неделя4_задание5', max_length=255, blank=True, unique=False)
    Week5_5 = models.CharField('Неделя5_задание5', max_length=255, blank=True, unique=False)
    Week6_5 = models.CharField('Неделя6_задание5', max_length=255, blank=True, unique=False)
    Week7_5 = models.CharField('Неделя7_задание5', max_length=255, blank=True, unique=False)
    Week8_5 = models.CharField('Неделя8_задание5', max_length=255, blank=True, unique=False)
    Week9_5 = models.CharField('Неделя9_задание5', max_length=255, blank=True, unique=False)
    Week10_5 = models.CharField('Неделя10_задание5', max_length=255, blank=True, unique=False)
    Week11_5 = models.CharField('Неделя11_задание5', max_length=255, blank=True, unique=False)
    Week12_5 = models.CharField('Неделя12_задание5', max_length=255, blank=True, unique=False)
    Week13_5 = models.CharField('Неделя13_задание5', max_length=255, blank=True, unique=False)
    Week14_5 = models.CharField('Неделя14_задание5', max_length=255, blank=True, unique=False)
    Week15_5 = models.CharField('Неделя15_задание5', max_length=255, blank=True, unique=False)
    Week16_5 = models.CharField('Неделя16_задание5', max_length=255, blank=True, unique=False)
    Week17_5 = models.CharField('Неделя17_задание5', max_length=255, blank=True, unique=False)
    Week18_5 = models.CharField('Неделя18_задание5', max_length=255, blank=True, unique=False)

    Week1_6 = models.CharField('Неделя1_задание6', max_length=255, blank=True, unique=False)
    Week2_6 = models.CharField('Неделя2_задание6', max_length=255, blank=True, unique=False)
    Week3_6 = models.CharField('Неделя3_задание6', max_length=255, blank=True, unique=False)
    Week4_6 = models.CharField('Неделя4_задание6', max_length=255, blank=True, unique=False)
    Week5_6 = models.CharField('Неделя5_задание6', max_length=255, blank=True, unique=False)
    Week6_6 = models.CharField('Неделя6_задание6', max_length=255, blank=True, unique=False)
    Week7_6 = models.CharField('Неделя7_задание6', max_length=255, blank=True, unique=False)
    Week8_6 = models.CharField('Неделя8_задание6', max_length=255, blank=True, unique=False)
    Week9_6 = models.CharField('Неделя9_задание6', max_length=255, blank=True, unique=False)
    Week10_6 = models.CharField('Неделя10_задание6', max_length=255, blank=True, unique=False)
    Week11_6 = models.CharField('Неделя11_задание6', max_length=255, blank=True, unique=False)
    Week12_6 = models.CharField('Неделя12_задание6', max_length=255, blank=True, unique=False)
    Week13_6 = models.CharField('Неделя13_задание6', max_length=255, blank=True, unique=False)
    Week14_6 = models.CharField('Неделя14_задание6', max_length=255, blank=True, unique=False)
    Week15_6 = models.CharField('Неделя15_задание6', max_length=255, blank=True, unique=False)
    Week16_6 = models.CharField('Неделя16_задание6', max_length=255, blank=True, unique=False)
    Week17_6 = models.CharField('Неделя17_задание6', max_length=255, blank=True, unique=False)
    Week18_6 = models.CharField('Неделя18_задание6', max_length=255, blank=True, unique=False)
    subjects = models.ManyToManyField(SubjectsNames, blank=True, through='SemestersSubjects')

    def __str__(self):
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

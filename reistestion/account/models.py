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


class GroupNames(models.Model):
    GroupName = models.CharField('???????????????? ????????????', max_length=10)

    def __str__(self):
        return self.GroupName

    def get_absolut_url(self):
        return f'/gnew/{self.id}'

    class Meta:
        verbose_name = '????????????'
        verbose_name_plural = '????????????'


class SubjectsNames(models.Model):
    SubjectName = models.CharField('???????????????? ????????????????????', max_length=64)

    def __str__(self):
        return self.SubjectName

    class Meta:
        verbose_name = '????????????????????'
        verbose_name_plural = '????????????????????'


class ModelsNames(models.Model):
    ModelName = models.CharField('???????????????? ????????????', max_length=64)

    def __str__(self):
        return self.ModelName

    class Meta:
        verbose_name = '????????????'
        verbose_name_plural = '????????????'


class ThemesNames(models.Model):
    ThemeName = models.CharField('???????????????? ????????', max_length=64)

    def __str__(self):
        return self.ThemeName

    class Meta:
        verbose_name = '????????'
        verbose_name_plural = '????????'


class TasksNames(models.Model):
    TaskName = models.CharField('???????????????? ??????????????', max_length=64)
    TaskName = models.TextField('???????????????? ??????????????', max_length=1024)
    TaskName = models.IntegerField('???????????????????????? ???????? ???? ??????????????')

    def __str__(self):
        return self.TaskName

    class Meta:
        verbose_name = '??????????????'
        verbose_name_plural = '????????????????'


class LessonsNames(models.Model):
    LessonName = models.DateTimeField('???????? ?? ?????????? ???????????????????? ????????')
    TaskName = models.IntegerField('?????????? ????????')

    def __str__(self):
        return self.LessonName

    class Meta:
        verbose_name = '????????'
        verbose_name_plural = '????????'


class GroupsSubjects(models.Model):
    Group = models.ForeignKey("GroupNames", on_delete=models.PROTECT, null=True, verbose_name='Group_key')
    Subject = models.ForeignKey("SubjectsNames", on_delete=models.PROTECT, null=True, verbose_name='Subject_key')

    def __str__(self):
        return self.Subject


class SubjectsTeachers(models.Model):
    Subject = models.ForeignKey("SubjectsNames", on_delete=models.PROTECT, null=True, verbose_name='Subject_key')
    Teacher = models.ForeignKey("Account", on_delete=models.PROTECT, null=True, verbose_name='Teacher_key')

    def __str__(self):
        return self.Teacher


class SubjectsModules(models.Model):
    Subject = models.ForeignKey("SubjectsNames", on_delete=models.PROTECT, null=True, verbose_name='Subject_key')
    Module = models.ForeignKey("ModelsNames", on_delete=models.PROTECT, null=True, verbose_name='Module_key')

    def __str__(self):
        return self.Module


class ModuleThemes(models.Model):
    Model = models.ForeignKey("ModelsNames", on_delete=models.PROTECT, null=True, verbose_name='Module_key')
    Theme = models.ForeignKey("ThemesNames", on_delete=models.PROTECT, null=True, verbose_name='Theme_key')

    def __str__(self):
        return self.Theme


class ThemesLessons(models.Model):
    Theme = models.ForeignKey("ThemesNames", on_delete=models.PROTECT, null=True, verbose_name='Theme_key')
    Lesson = models.ForeignKey("LessonsNames", on_delete=models.PROTECT, null=True, verbose_name='Lessons_key')

    def __str__(self):
        return self.Lesson


class LessonsTasks(models.Model):
    Lesson = models.ForeignKey("LessonsNames", on_delete=models.PROTECT, null=True, verbose_name='Lessons_key')
    Task = models.ForeignKey("TasksNames", on_delete=models.PROTECT, null=True, verbose_name='Task_key')

    def __str__(self):
        return self.Task


class TasksStudents(models.Model):
    Task = models.ForeignKey("TasksNames", on_delete=models.PROTECT, null=True, verbose_name='Task_key')
    Student = models.ForeignKey("Account", on_delete=models.PROTECT, null=True, verbose_name='Students_key')
    Mark = models.IntegerField("????????????")

    def __str__(self):
        return self.Task, self.Student, self.Mark

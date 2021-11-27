from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, ImageForm, SubjectsNamesForm, \
    GroupsSubjectsForm, SubjectsTeachersForm, SemestersSubjectsForm, ThemesNamesForm, ModulesNamesForm, \
    SubjectsModulesForm, LessonsNamesForm, TasksNamesForm, ModuleThemesForm, ThemesLessonsForm, LessonsTasksForm, \
    TasksStudentsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from .models import GroupNames, Semester
from .forms import GroupForm, TableUpdateForm
from django.db import IntegrityError
from .models import Account


def registration_view(request):
    context = {}
    if request.method == 'GET':
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'account/register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            phn = request.POST['phone_no'].replace(" ", "")
            try:
                user = Account.objects.create_user(request.POST['email'],
                                                   password=request.POST['password1'],
                                                   username=request.POST['username'],
                                                   gender=request.POST['gender'],
                                                   phone_no=phn,
                                                   prof_img=None,)
                user.save()
                login(request, user)
                return redirect('image')
            except IntegrityError:
                return render(request, 'account/register.html', {'form': RegistrationForm()})
        else:
            return render(request, 'account/register.html', {'form': RegistrationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "account/login.html", context)


def image_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = ImageForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = ImageForm()
        context['account_form'] = form
        return render(request, "account/image.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "gender": request.POST['gender'],
                "phone_no": request.POST['phone_no'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "gender": request.user.gender,
                "phone_no": request.user.phone_no,
                "prof_img": request.user.prof_img,
            })

    context['account_form'] = form
    return render(request, "account/account.html", context)


def interface(request):
    gnew = GroupNames.objects.order_by('-id')
    return render(request, "account/interface.html", {'gnew': gnew})


class dinamic(DetailView):
    model = GroupNames
    template_name = 'account/din.html'
    context_object_name = 'arti'


class update(UpdateView):
    model = GroupNames
    template_name = 'account/update.html'
    form_class = GroupForm


class delete(DeleteView):
    model = GroupNames
    success_url = '/account'
    template_name = 'account/group-delite.html'
    form_class = GroupForm


def group(request):
    if request.method == 'POST':
        gform = GroupForm(request.POST)
        if gform.is_valid():
            gform.save()
            return redirect('/account')

    gform = GroupForm()

    gdata = {
        'gform': gform,
    }

    return render(request, 'account/group.html', gdata)


def table_view(request):
    if request.method == 'POST':
        qform = TableUpdateForm(request.POST)
        if qform.is_valid():
            qform.save()
            return redirect('/account')

    qform = TableUpdateForm()

    qdata = {
        'qform': qform,
    }

    return render(request, 'account/table.html', qdata)


def subjects_names_view(request):
    if request.method == 'POST':
        form = SubjectsNamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = SubjectsNamesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/subject-name.html', data)


def groups_subjects_view(request):
    if request.method == 'POST':
        form = GroupsSubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = GroupsSubjectsForm()

    data = {
        'form': form,
    }

    return render(request, 'account/groups-subjects.html', data)


def subjects_teachers_view(request):
    if request.method == 'POST':
        form = SubjectsTeachersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = SubjectsTeachersForm()

    data = {
        'form': form,
    }

    return render(request, 'account/subjects-teachers.html', data)


def semesters_subjects_view(request):
    if request.method == 'POST':
        form = SemestersSubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = SemestersSubjectsForm()

    data = {
        'form': form,
    }

    return render(request, 'account/semesters-subjects.html', data)


def themes_names_view(request):
    if request.method == 'POST':
        form = ThemesNamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = ThemesNamesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/themes-names.html', data)


def modules_names_view(request):
    if request.method == 'POST':
        form = ModulesNamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = ModulesNamesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/modules-names.html', data)


def subjects_modules_view(request):
    if request.method == 'POST':
        form = SubjectsModulesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = SubjectsModulesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/subjects-modules.html', data)


def lessons_names_view(request):
    if request.method == 'POST':
        form = LessonsNamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = LessonsNamesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/lessons-names.html', data)


def tasks_names_view(request):
    if request.method == 'POST':
        form = TasksNamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = TasksNamesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/tasks-names.html', data)


def modules_themes_view(request):
    if request.method == 'POST':
        form = ModuleThemesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = ModuleThemesForm()

    data = {
        'form': form,
    }

    return render(request, 'account/modules-themes.html', data)


def themes_lessons_view(request):
    if request.method == 'POST':
        form = ThemesLessonsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = ThemesLessonsForm()

    data = {
        'form': form,
    }

    return render(request, 'account/themes-lessons.html', data)


def lessons_tasks_view(request):
    if request.method == 'POST':
        form = LessonsTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = LessonsTasksForm()

    data = {
        'form': form,
    }

    return render(request, 'account/lessons-tasks.html', data)


def tasks_students_view(request):
    if request.method == 'POST':
        form = TasksStudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    form = TasksStudentsForm()

    data = {
        'form': form,
    }

    return render(request, 'account/tasks-students.html', data)


def navigate(request):
    return render(request, 'account/navigation.html')

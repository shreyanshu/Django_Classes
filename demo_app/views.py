from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from demo_app.models import Student, Room
from demo_app.forms import StudentForm, LoginForm, RegistrationForm, RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

# Create your views here.
def contact_us(request):
    return HttpResponse("contact page")


@login_required(login_url='/d1/login/')
def list_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'list_students.html', {"students":students})


def add_student(request):
    if request.method == 'GET':
        student_form = StudentForm()
        return render(request, "add_student.html", {"form":student_form})
    elif request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Addition successful")
        return redirect('list_students')


def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        messages.success(request, "Deletion Successful")
        return redirect("list_students")
    except:
        messages.error(request, "student with id "+str(id)+" not found")
        return redirect("list_students")


class EditStudent(LoginRequiredMixin, View):
    login_url = 'd1/login/'
    def get(self, request, id):
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request, 'edit_student.html', {"form":form, "student_id":id})

    def post(self, request, id):
        student = Student.objects.get(id=id)
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students')
        # else:


def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'login.html', {"login_form":login_form})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('list_students')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('user_login')


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_register(request):
    if request.method == 'GET':
        register_form = RegistrationForm()
        return render(request, 'register.html', {"register_form":register_form})

    elif request.method == 'POST':
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()
            return redirect('user_login')


class ListRooms(LoginRequiredMixin, ListView):

    login_url = '/d1/login/'
    template_name = 'list_room.html'
    queryset = Room.objects.all()


class RoomDetail(LoginRequiredMixin, DetailView):

    login_url = '/d1/login/'
    template_name = 'detail_room.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])


class ContactView(TemplateView):
     template_name = 'contact_us.html'


class RoomCreateView(LoginRequiredMixin, CreateView):

    login_url = '/d1/login/'
    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = '/d1/list_rooms/'

    # def get_success_url(self):
    #     return reverse('list_rooms')


class RoomUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'room_update.html'
    form_class = RoomForm
    login_url = '/d1/login/'

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])

    def get_success_url(self):
        return reverse('list_rooms')


class RoomDeleteView(LoginRequiredMixin, DeleteView):

    login_url = '/d1/login/'
    template_name = 'delete_room.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Room, id=self.kwargs['id'])

    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('list_rooms')

    def post(self, request, *args, **kwargs):
        try:
            room = Room.objects.get(id = self.kwargs['id'])
            room.delete()
            return redirect('list_rooms')
        except:
            messages.error(request, "Can't delete this room")
            return redirect('list_rooms')


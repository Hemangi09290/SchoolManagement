from django.shortcuts import render
from django.urls import reverse_lazy

from workonformapp.models import Student, Country, City
from .forms import StudentForm
from .forms import InputForm
from django.views.generic import ListView, CreateView, UpdateView

#from .models import 

# Create your views here.
def index(request):
    #num_authors = Author.objects.count()  # The 'all()' is implied by default.
   
    # Render the HTML template index.html with the data in the context variable.
    #return render(request, 'index.html')
    return

def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)

class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')


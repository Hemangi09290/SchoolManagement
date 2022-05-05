from multiprocessing import context
from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from workonformapp.models import Student, Country, City
from .forms import StudentForm
from .forms import InputForm
from django.views.generic import ListView, CreateView, UpdateView
# relative import of forms
from .models import Student

#from .models import 

# Create your views here.
#def index(request):
    #num_authors = Author.objects.count()  # The 'all()' is implied by default.
   
    # Render the HTML template index.html with the data in the context variable.
    #return render(request, 'index.html')
#    return

#THis is basic example of how we can use InputForm 

# class StudentListView(ListView):
#     model = Student
#     form_class = StudentForm
#     context_object_name = 'students'
#     render(request, 'student_list.html')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_change_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_change_list')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id)
    return render(request, 'student_list.html', {'cities':cities})


def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}
	# add the dictionary during initialization
	context["students"] = Student.objects.all()
	return render(request, "student_list.html", context)

def create_viewold(request):
	context ={}
	context['students']= StudentForm()
	return render(request, "student_form.html", context)

def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('student_change_list'))
          
    context['students']= form
    print(context)
    return render(request, "student_form.html", context)

# update view for details
def update_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Student, id = pk)
 
    # pass the object as instance in form
    form = StudentForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('student_change_list'))
         
 
    # add form dictionary to context
    context["students"] = form
 
    return render(request, "student_form.html", context)
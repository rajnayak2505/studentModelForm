from django.shortcuts import render
from testapp.forms import StudentForm
from testapp.models import Student

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html')

def add_student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request, 'testapp/addstudent.html', {'form':form})

def list_student_view(request):
    student_list = Student.objects.all()
    return render(request, 'testapp/liststudent.html', {'student_list':student_list})

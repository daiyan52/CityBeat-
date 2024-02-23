from django.shortcuts import render
from testapp.forms import EmployeeForm
from testapp.feedbackForm import feedback_form
from testapp.models import Kolkata_job,Delhi_job,Bengaluru_job,Hyderabad_job,feedback
# Create your views here.
def Home_View(request):
    return render(request, 'HtmlFolder/home.html')

def Kolkata_View(request):
    job_list = Kolkata_job.objects.all()
    my_dict = {'job_list': job_list}
    return render(request, 'HtmlFolder/Kolkata_jobs.html',my_dict)

def Delhi_View(request):
    job_list = Delhi_job.objects.all()
    my_dict = {'job_list': job_list}
    return render(request, 'HtmlFolder/DelhiJobs.html',my_dict)





def EmployeeForm_view(request):
    submitted = False
    fname = ''
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid(): 
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['marks'])
            fname = form.cleaned_data['First_Name']
            submitted = True
    # form = EmployeeForm()
    my_dict = {'form': form,'fname': fname,'submitted': submitted}
    return render(request, 'HtmlFolder/form.html', my_dict)

def feedback_view(request):
    form = feedback_form()
    submitted = False
    name = ''
    if request.method == 'POST':
          form = feedback_form(request.POST)
          if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name)
            print(email)
            print(message)
            submitted = True
            print('Feedback submitted successfully')
    
    form = feedback_form()
    my_dict = {'form': form,'name': name,'submitted': submitted}
    return render(request, 'HtmlFolder/feedback.html', my_dict)
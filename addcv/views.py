from django.shortcuts import render
<<<<<<< HEAD
from .forms import personalform, educationform, experienceform, whole
from .models import experience, education, person, FilesUpload
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

=======
from .forms import personalform, educationform, experienceform, projectform, resumeform
from .models import experience, education, person
>>>>>>> upstream/master
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
import datetime

def createcv(request):
    return render(request, 'addcv/cv.html')
def personal(request):
    if request.method == 'POST':
        fm = personalform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'addcv/personal.html',{'form':fm})
    else:
        fm = personalform()
        #em = educationform()
        return render(request,'addcv/personal.html',{'form':fm})


def educational(request):
    if request.method == 'POST':
        fm = educationform(request.POST)
        #em = educationform(request.POST)
        if fm.is_valid():
            fm.save()

        return render(request, 'addcv/educational.html', {'form':fm})
    else:
        fm = educationform()
        #em = educationform()
        return render(request,'addcv/educational.html',{'form':fm})

def experiences(request):
    if request.method == 'POST':
        fm = experienceform(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'addcv/experience.html',{'form':fm})
    else:
        fm = experienceform()
        #em = educationform()
        return render(request,'addcv/experience.html',{'form':fm})

def project(request):
    if request.method == 'POST':
        fm = projectform(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'addcv/project.html',{'form':fm})
    else:
        fm = projectform()
        #em = educationform()
        return render(request,'addcv/project.html',{'form':fm})

def resumes(request):
    if request.method == 'POST':
        fm = resumeform(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'addcv/resume.html',{'form':fm})
    else:
        fm = resumeform()
        #em = educationform()
        return render(request,'addcv/resume.html',{'form':fm})

def cv(request):
    context = {
        'persons': persons.objects.all(),
        'experiences': experiences.objects.all(),
        'educations' : educations.objects.all()
    }
    return render(request, 'resumes/2/index.html', context)

def upload(request):
    
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        document = FilesUpload.objects.create(file=uploaded_file)
        document.save()
        return HttpResponse("your file was saved")
        
    return render(request, 'seavs/upload.html')


# Create your views here.

def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Addcv'+\
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'


    html_string=render_to_string('resumes/2/pdf-output.html')
    html=HTML(string=html_string)

    result = html.write_pdf()


    with tempfile.NamedTemporaryFile(delete=True)as output:
        output.write(result)
        output.flush()

        output=open(output.name,'rb')

        response.write(output.read())


    return response
